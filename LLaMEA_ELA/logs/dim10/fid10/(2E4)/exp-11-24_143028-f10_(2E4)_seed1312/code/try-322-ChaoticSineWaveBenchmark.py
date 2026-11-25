import numpy as np

class ChaoticSineWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sine-wave parameters
        self.freqs = np.random.uniform(2.0, 10.0, dim)
        self.amps = np.random.uniform(0.5, 3.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Adaptive conditioning with exponential scaling
        self.conditioning = np.random.uniform(0.1, 15.0, dim)
        # Multi-modal structure with chaotic peaks
        self.modal_centers = np.random.uniform(-4.0, 4.0, (dim, 5))
        self.modal_weights = np.random.dirichlet(np.ones(5), dim).T
        # Cross-dimension coupling with chaotic interaction
        self.coupling_strength = np.random.uniform(0.1, 1.0, (dim, dim))
        np.fill_diagonal(self.coupling_strength, 0.0)
        # Chaotic parameter for enhanced complexity
        self.chaos_factor = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for sine components
        normalized_x = x / 5.0
        
        # Compute chaotic sine-wave components
        sine_components = np.zeros(self.dim)
        for i in range(self.dim):
            # Base chaotic sine term with exponential conditioning
            sine_components[i] = self.amps[i] * np.sin(
                self.freqs[i] * normalized_x[i] + self.phases[i]
            ) * (self.conditioning[i]**(1.2))
            
        # Multi-modal structure with chaotic peaks
        modal_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Weighted sum of modal contributions with chaotic decay
            modal_sum = 0.0
            for j in range(5):
                dist = np.abs(normalized_x[i] - self.modal_centers[i, j])
                modal_sum += self.modal_weights[j, i] * np.exp(-dist**2 / 0.03)
            modal_values[i] = modal_sum
            
        # Combine components with chaotic mixing
        fitness = 0.0
        for i in range(self.dim):
            # Add sine and modal components with chaotic interaction
            component_value = sine_components[i] + modal_values[i]
            fitness += component_value**2
            
        # Add cross-dimension coupling with chaotic sine-cosine interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_strength[i, j] * (
                        np.sin(sine_components[i]) * np.cos(sine_components[j])
                    )
                    
        # Add chaotic scaling and noise
        return fitness + 0.2 * coupling_term + 0.1 * np.sum(np.sin(self.chaos_factor * x)**3)