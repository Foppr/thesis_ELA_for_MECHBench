import numpy as np

class FractalGeneticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dimension = 2.3
        self.genetic_mutation_rate = 0.15
        self.fractional_order = 0.7
        self.num_generations = 5
        self.scale_factor = 2.0
        self.chaotic_parameter = 3.9
        self.noise_level = 0.05
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        result = 0.0
        
        # Chaotic fractal component with logistic map
        chaotic_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Logistic map chaos modulation
            chaotic_val = np.sin(xi * np.pi / 5.0) * np.cos(xi * np.pi / 3.0)
            chaotic_sum += chaotic_val * np.exp(-0.1 * i)
        
        # Genetic algorithm inspired component with multi-scale mutation
        genetic_component = 0.0
        for gen in range(self.num_generations):
            mutation_strength = self.genetic_mutation_rate * (1.0 - gen / self.num_generations)
            for i in range(self.dim):
                # Multi-scale genetic mutation with chaotic influence
                scale = np.power(self.scale_factor, gen)
                chaotic_influence = np.sin(gen * np.pi / 5.0)
                gene_val = x[i] + mutation_strength * scale * chaotic_influence * np.random.randn()
                # Fitness contribution with genetic operator
                genetic_component += np.sin(gene_val) * np.cos(gene_val * 0.5) * np.exp(-gen / self.num_generations)
        
        # Self-similar fractal landscape component with chaotic scaling
        fractal_landscape = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-fractal scaling with chaotic exponents
            for k in range(3, 8):
                # Chaotic scaling factor
                chaotic_scale = np.sin(k * self.chaotic_parameter) * 0.5 + 0.5
                scale_k = np.power(2.0, -k * self.fractal_dimension) * chaotic_scale
                fractal_landscape += scale_k * np.sin(xi * np.power(2.0, k)) * np.cos(xi * np.power(3.0, k))
        
        # Cross-dimensional interaction with fractal correlation and chaos
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal correlation between dimensions with chaotic modulation
                corr_val = np.sin(np.pi * (x[i] + x[j]) / 10.0) * np.cos(np.pi * (x[i] - x[j]) / 10.0)
                # Chaotic modulation of correlation
                chaotic_mod = np.sin(np.pi * (x[i] + x[j]) / 5.0)
                corr_val *= chaotic_mod
                dist = np.abs(x[i] - x[j])
                cross_term += corr_val * np.exp(-dist * 0.5)
        
        # Temporal-like evolution component with fractal time scaling and chaos
        temporal_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal temporal modulation with chaotic influence
            t_mod = np.sin(np.pi * xi / 5.0) * np.cos(np.pi * xi / 3.0)
            chaotic_influence = np.sin(xi * self.chaotic_parameter)
            temporal_component += t_mod * np.sin(xi * 2.0 + t_mod + chaotic_influence) * np.cos(xi * 1.5 + t_mod + chaotic_influence)
        
        # Add noise to make landscape more challenging
        noise = np.random.normal(0, self.noise_level, self.dim)
        noise_component = np.sum(noise * x) * 0.1
        
        # Combine all components with adjusted weights for better fitness
        return 0.35 * chaotic_sum + 0.3 * genetic_component + 0.25 * fractal_landscape + 0.07 * cross_term + 0.03 * temporal_component + noise_component