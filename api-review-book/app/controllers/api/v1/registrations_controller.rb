class Api::V1::RegistrationsController < Devise::RegistrationsController

  before_action :ensure_params_exist, only: :create

  def create
    user = User.new user_params

    if user.save
      json_response "Sign Up Succcessfully", true, { user: user }, :ok
    else
      json_response "email or password is invalid. Please try again", false, {}, :unprocessable_entity
    end
  end

  private

  def user_params
    params.require(:user).permit(:email, :password, :password_confirmation)
  end

  def ensure_params_exist
    return if params[:user].present?

    render json: {
      message: "Missing params",
      is_success: false
    }, status: :bad_request
  end
end