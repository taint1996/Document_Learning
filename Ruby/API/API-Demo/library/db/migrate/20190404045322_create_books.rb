class CreateBooks < ActiveRecord::Migration[5.2]
  def change
    create_table :books do |t|
      t.string :title
      t.string :author
      t.string :weight
      t.string :publisher
      t.string :language
      t.integer :pages
      t.datetime :publication_date

      t.timestamps
    end
  end
end
