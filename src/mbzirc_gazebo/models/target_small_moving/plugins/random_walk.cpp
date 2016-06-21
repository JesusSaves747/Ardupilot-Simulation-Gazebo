#include <boost/bind.hpp>
#include <gazebo/gazebo.hh>
#include <gazebo/physics/physics.hh>
#include <gazebo/common/common.hh>
#include <stdio.h>
#include <random>

namespace gazebo
{
  class RandomWalk : public ModelPlugin
  {
    public:

      RandomWalk() : random_engine(std::random_device()()), speed_distribution(-MaxSpeed, MaxSpeed), test_distribution(0.0, 1.0)
      {
      }

      void Load(physics::ModelPtr _parent, sdf::ElementPtr /*_sdf*/)
      {
        // Store the pointer to the model
        this->model = _parent;

        // Listen to the update event. This event is broadcast every simulation iteration.
        this->update_connection = event::Events::ConnectWorldUpdateBegin(
            boost::bind(&RandomWalk::OnUpdate, this, _1));
      }

      // Called by the world update start event
      void OnUpdate(const common::UpdateInfo & /*_info*/)
      {
        // Apply a small linear velocity to the model sometimes.
        if (this->test_distribution(random_engine) > 0.9)
        {
          float x_velocity = this->speed_distribution(random_engine);
          float y_velocity = this->speed_distribution(random_engine);
          this->model->SetLinearVel(math::Vector3(x_velocity, y_velocity, 0.0));
        }
      }

    private:

      static constexpr const float MaxSpeed = 1.38889;
      physics::ModelPtr model;
      event::ConnectionPtr update_connection;
      std::default_random_engine random_engine;
      std::uniform_real_distribution<float> speed_distribution;
      std::uniform_real_distribution<float> test_distribution;
  };

  // Register this plugin with the simulator
  GZ_REGISTER_MODEL_PLUGIN(RandomWalk)
}
