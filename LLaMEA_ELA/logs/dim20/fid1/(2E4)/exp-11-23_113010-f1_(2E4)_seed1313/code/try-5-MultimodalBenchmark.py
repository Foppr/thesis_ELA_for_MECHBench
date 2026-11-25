import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial term with varying exponents for complexity
        poly_term = np.sum(np.abs(x_norm)**(2 + np.arange(self.dim) % 4))
        
        # High-frequency trigonometric components creating many local optima
        trig_term = np.sum(np.sin(10 * np.pi * x_norm)**2 + 
                          np.cos(7 * np.pi * x_norm)**2 + 
                          np.sin(3 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm))
        
        # Coupled sine-cosine products with phase shifts
        coupled_term = np.sum(np.sin(x_norm[:-1] + x_norm[1:]) * 
                             np.cos(x_norm[:-1] - x_norm[1:]))
        
        # Exponential penalty for values near boundaries
        boundary_penalty = np.sum(np.exp(2 * np.abs(x_norm)) * (np.abs(x_norm) > 0.8))
        
        # Chaotic interaction term using golden ratio and modular arithmetic
        chaotic_term = 0.0
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        for i in range(self.dim):
            chaotic_term += np.sin(phi * x_norm[i] * (i + 1)) * np.cos((i + 1) * x_norm[i] / phi)
        
        # Add stochastic perturbation with deterministic pattern
        stochastic_perturbation = 0.3 * np.random.uniform(-1, 1) * np.mean(np.sin(x_norm))
        
        # Combine all terms with carefully tuned weights
        result = 2.0 * poly_term + 1.5 * trig_term + 0.8 * coupled_term + 0.5 * boundary_penalty + 0.3 * chaotic_term + stochastic_perturbation
        
        return result