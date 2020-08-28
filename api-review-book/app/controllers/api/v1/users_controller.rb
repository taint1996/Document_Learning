class Api::V1::UsersController < ApplicationController
  def fb
    if params[:facebook_access_token]
      graph = Koala::Facebook::API.new params[:facebook_access_token]

      user_data = graph.get_object("me?fields=name,email,id,picture")
      user = User.find_by(email: user_data[:email])
      p user_data["email"]
      if user
        user.generate_authentication_token
        json_response_success "User Information", { user: user }
      else
        p ">>>>>>>>>>>>>> user_data #{user_data}"
        user = User.new(  email: "test_api@api.vn",
                          password: Devise.friendly_token[0, 20],
                          image: user_data["picture"]["data"]["url"],
                          uid: user_data["id"],
                          provider: "facebook"
                        )
        user.authentication_token = User.generate_unique_secure_token

        if user.save
          json_response_success "Login FB succesfully", { user: user }
        else
          json_response_error user.errors, :unprocessable_entity
        end
      end
    else
      json_response_error "Missing facebook access token", :unprocessable_entity
    end
  end
end