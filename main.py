import Index.read_json as read
import Index.statistics as stat
import Index.tokenize_func as tkn

file_json_url = "crawled_urls.json"
number_of_doc = 20

list_of_url = read.part_list(read.read_json(file_json_url), number_of_doc)
index_non_pos = tkn.index_non_pos(tkn.list_title(list_of_url))
index_pos = tkn.index_pos(tkn.list_title(list_of_url))
statistics = stat.create_dico_stat(index_non_pos, list_of_url)

read.create_json(index_non_pos, "title.non_pos_index.json")
read.create_json(index_pos, "title.pos_index.json")
read.create_json(statistics, "metadata.json")
