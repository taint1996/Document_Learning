Rails.application.routes.draw do  
  api_version(:module => "V1", :path => {:value => "v1"}) do
  end  
  resources :books
end
