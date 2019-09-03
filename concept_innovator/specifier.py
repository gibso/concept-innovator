from concept_innovator import conceptnet_adapter
import tempfile

def specify_mental_space(mental_space):
     local_spec = f'spec {mental_space.name} = Global then\n ops'

     for concept in mental_space.involved_concepts:
        local_spec += f'{concept} : Concept\n'

     for fact in mental_space.facts:
         local_spec += f'. {concept} : Concept\n'

     return 'halodri'


def create_casl_for_input_spaces(input_spaces, domain):
    f = open("innovation.casl", "w+")

    domain_spec_name = domain.capitalize()

    input_space_specs = []
    related_terms = []
    for input_space in input_spaces:
        print(f'start collecting spec information for node: "{input_space["label"]}')
        input_space_spec_name = input_space['label'].capitalize()
        input_space_spec = f'spec {input_space_spec_name} = {domain_spec_name} then\n  op c:{domain_spec_name}\n'

        for relation in all_relations:
            print(f'get relations for relation "{relation}"')
            related_nodes = conceptnet_adapter.find_related_nodes_for(input_space, relation)
            for related_node in related_nodes:
                input_space_spec += f'  . {relation}(c, {related_node["label"]})\n'
                related_terms.append(related_node["label"])

        input_space_spec += 'end\n\n'
        input_space_specs.append(input_space_spec)

    domain_spec = create_spec_for_domain(domain)
    semsys_spec = create_semsys_spec()
    symbols_spec = create_symbols_spec(related_terms)

    spec = f'{semsys_spec}\n\n{symbols_spec}\n\n{domain_spec}\n\n'

    for input_space_spec in input_space_specs:
        spec += input_space_spec

    f.write(spec)
    f.close()
    return None


def create_spec_for_domain(domain):
    spec_name = domain.capitalize()
    spec = f'spec {spec_name} = Symbols then\n  sort Animal\n  preds\n'
    for relation in all_relations:
        spec += f'    {relation} : {spec_name} * Term\n'
    spec += 'end'
    return spec


def create_semsys_spec():
    return'spec SemSys =\n  sort PriorityDummySort\n  op prioDummyOp : PriorityDummySort\nend'


def create_symbols_spec(terms):
    spec = 'spec Symbols = SemSys then\n  generated type Term ::= '
    for term in terms:
        spec += f'{term} | '
    spec = spec[:-3]
    spec += '\nend'
    return spec