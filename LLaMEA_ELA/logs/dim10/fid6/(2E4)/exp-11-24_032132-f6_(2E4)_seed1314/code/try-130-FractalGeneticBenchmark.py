import numpy as np

class FractalGeneticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dimension = 2.3
        self.genetic_mutation_rate = 0.15
        self.fractional_order = 0.7
        self.num_generations = 5
        self.scale_factor = 2.0
        self.chaos_factor = 0.1
        self.interaction_strength = 0.5
        
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
        
        # Fractal-based polynomial component with fractional calculus
        fractal_sum = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractional power scaling with fractal dimension
            frac_power = np.power(np.abs(xi), self.fractional_order)
            # Fractal modulation based on dimension index
            fractal_mod = np.sin(xi * np.pi / 5.0) * np.cos(xi * np.pi / 3.0)
            fractal_sum += (frac_power + 0.5 * fractal_mod) * np.exp(-0.1 * i)
        
        # Genetic algorithm inspired component with multi-scale mutation
        genetic_component = 0.0
        for gen in range(self.num_generations):
            mutation_strength = self.genetic_mutation_rate * (1.0 - gen / self.num_generations)
            for i in range(self.dim):
                # Multi-scale genetic mutation
                scale = np.power(self.scale_factor, gen)
                gene_val = x[i] + mutation_strength * scale * np.random.randn()
                # Fitness contribution with genetic operator
                genetic_component += np.sin(gene_val) * np.cos(gene_val * 0.5) * np.exp(-gen / self.num_generations)
        
        # Self-similar fractal landscape component with chaotic modulation
        fractal_landscape = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-fractal scaling with different exponents and chaotic factor
            for k in range(3, 8):
                scale_k = np.power(2.0, -k * self.fractal_dimension)
                chaos_mod = np.sin(xi * self.chaos_factor * k) * np.cos(xi * self.chaos_factor * k)
                fractal_landscape += scale_k * np.sin(xi * np.power(2.0, k)) * np.cos(xi * np.power(3.0, k)) * chaos_mod
        
        # Cross-dimensional interaction with fractal correlation and chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal correlation between dimensions with chaotic modulation
                corr_val = np.sin(np.pi * (x[i] + x[j]) / 10.0) * np.cos(np.pi * (x[i] - x[j]) / 10.0)
                dist = np.abs(x[i] - x[j])
                # Add chaotic coupling term
                chaos_coupling = np.sin(np.pi * (x[i] * x[j]) / 25.0)
                cross_term += corr_val * np.exp(-dist * 0.5) * chaos_coupling
        
        # Temporal-like evolution component with fractal time scaling and chaotic dynamics
        temporal_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractal temporal modulation with chaotic factor
            t_mod = np.sin(np.pi * xi / 5.0) * np.cos(np.pi * xi / 3.0)
            chaos_temporal = np.sin(xi * self.chaos_factor) * np.cos(xi * self.chaos_factor)
            temporal_component += t_mod * np.sin(xi * 2.0 + t_mod) * np.cos(xi * 1.5 + t_mod) * chaos_temporal
        
        # Add chaotic noise component
        noise_component = 0.0
        for i in range(self.dim):
            xi = x[i]
            noise_component += np.sin(xi * self.chaos_factor * 10.0) * np.cos(xi * self.chaos_factor * 10.0)
        
        # Combine all components with updated weights
        return 0.35 * fractal_sum + 0.25 * genetic_component + 0.25 * fractal_landscape + 0.1 * cross_term + 0.04 * temporal_component + 0.01 * noise_component