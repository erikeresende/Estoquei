from git_filter_repo import FilterRepo, Commit

def filter_repo(repo):
    # Obtenha o commit inicial
    initial_commit = repo.get_root_commit()

    # Alterar o autor do commit inicial
    if initial_commit:
        initial_commit.author_name = "Érike Resende"
        initial_commit.author_email = "erike2000augusto@gmail.com"
        initial_commit.committer_name = "Érike Resende"
        initial_commit.committer_email = "erike2000augusto@gmail.com"

# Execute o filtro
FilterRepo(filter_repo).run()
