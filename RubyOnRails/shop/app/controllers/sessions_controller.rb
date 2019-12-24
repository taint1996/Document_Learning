class SessionsController < ApplicationController
  def new
  end

  def create
    user = User.find_by(email: params[:email])

    if user && user.authentication(params[:password])
      session[:user_id] = user.id
      redirect_to root_url, notice: 'You are login!'
    else
      flash.now[:alert] = "Email or password is invalid. Please try again"
      render :new
    end
  end

  def destroy
    session[:user_id] = nil
    redirect_to root_url, notice: 'Logged out'
  end
end
