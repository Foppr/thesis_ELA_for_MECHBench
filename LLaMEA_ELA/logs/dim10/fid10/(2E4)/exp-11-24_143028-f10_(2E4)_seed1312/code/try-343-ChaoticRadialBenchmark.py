import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for non-linearity
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        # Radial components with varying strengths
        self.radial_strength = np.random.uniform(0.5, 2.0, dim)
        self.radial_freq = np.random.uniform(1.0, 3.0, dim)
        # Sinusoidal components with multiple frequencies
        self.sin_freq = np.random.uniform(2.0, 8.0, (dim, 3))
        self.sin_amp = np.random.uniform(0.5, 1.5, (dim, 3))
        # Cross-dimension coupling with chaotic interaction
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, (dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0.0)
        # Shifted local minima positions
        self.minima_positions = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.minima_heights = np.random.uniform(0.1, 2.0, 5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for internal computations
        normalized_x = x / 5.0
        
        # Compute radial component with chaotic modulation
        r = np.sqrt(np.sum(normalized_x**2))
        radial_term = np.sum(self.radial_strength * np.sin(self.radial_freq * r) * 
                           (1 + 0.3 * np.sin(5 * r)))
        
        # Compute multi-frequency sinusoidal components
        sin_terms = np.zeros(self.dim)
        for i in range(self.dim):
            term = 0.0
            for j in range(3):
                term += self.sin_amp[i, j] * np.sin(self.sin_freq[i, j] * normalized_x[i])
            sin_terms[i] = term
        
        # Combine sinusoidal and radial components
        combined = sin_terms + radial_term
        
        # Add chaotic cross-dimension coupling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling += self.coupling_matrix[i, j] * (
                        np.sin(combined[i]) * np.cos(combined[j]) + 
                        self.chaotic_params[i] * np.sin(combined[i] * combined[j])
                    )
        
        # Add local minima landscape
        minima_penalty = 0.0
        for i in range(5):
            dist = np.sum((normalized_x - self.minima_positions[:, i])**2)
            minima_penalty += self.minima_heights[i] * np.exp(-dist / 0.3)
        
        # Final fitness computation with chaotic perturbations
        fitness = np.sum(combined**2) + 0.5 * coupling + minima_penalty
        
        # Add chaotic noise term
        noise = 0.1 * np.sum(np.sin(10 * x) * np.cos(7 * x))
        
        return fitness + noise