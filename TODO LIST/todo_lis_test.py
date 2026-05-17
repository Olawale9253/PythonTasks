import from 






    self.assertEquals(all_task, 0)

  def test_that_task_is_created(self):

    title = "Write Code"

    content = "Write EOB's assignment snacks"

    confirmation_code = create_task(title, content, 1s)
    
    available_task = count_task()

    self.assertEquals(confirmation_code, 0)

    self.assertEquals(available_task, 1)
