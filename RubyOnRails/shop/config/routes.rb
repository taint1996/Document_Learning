Rails.application.routes.draw do
  root 'home#index'

  get 'sessions/new'
  get 'sessions/create'
  get 'sessions/destroy'

  resources :users
  resources :sessions
end
