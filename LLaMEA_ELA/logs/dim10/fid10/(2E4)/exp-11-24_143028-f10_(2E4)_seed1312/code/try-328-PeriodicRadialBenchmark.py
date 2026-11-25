import numpy as np

class PeriodicRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced periodic parameters with chaotic modulation
        self.frequencies = np.random.uniform(2.0, 10.0, dim)
        self.amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.phases = np.random.uniform(0, 4*np.pi, dim)
        # Radial parameters with chaotic scaling
        self.radial_freq = np.random.uniform(1.0, 5.0, dim)
        self.radial_amp = np.random.uniform(0.2, 1.5, dim)
        # Stronger conditioning with chaotic variation
        self.conditioning = np.random.uniform(0.5, 15.0, dim)
        # Multi-modal structure with chaotic center distribution
        self.modal_centers = np.random.uniform(-4.0, 4.0, (dim, 5)) + np.sin(np.arange(dim) * 0.7)
        self.modal_weights = np.random.dirichlet(np.ones(5), dim).T
        # Increased coupling strength with chaotic interaction terms
        self.coupling_strength = np.random.uniform(0.6, 1.2, (dim, dim))
        np.fill_diagonal(self.coupling_strength, 0.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for periodic components
        normalized_x = x / 5.0
        
        # Compute radial component with chaotic modulation
        r = np.sqrt(np.sum(normalized_x**2))
        radial_component = np.sum(self.radial_amp * np.sin(self.radial_freq * r + np.sin(r * 3)))
        
        # Compute periodic components with chaotic cubic nonlinearities
        periodic_components = np.zeros(self.dim)
        for i in range(self.dim):
            # Base periodic term with chaotic cubic modulation
            base_term = self.amplitudes[i] * np.sin(
                self.frequencies[i] * normalized_x[i] + self.phases[i]
            )
            cubic_term = 0.6 * np.sin(3 * self.frequencies[i] * normalized_x[i]) + 0.2 * np.cos(5 * self.frequencies[i] * normalized_x[i])
            periodic_components[i] = (base_term + cubic_term) * self.conditioning[i]
            
        # Multi-modal structure with chaotic response
        modal_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Weighted sum of modal contributions with chaotic interaction
            modal_sum = 0.0
            for j in range(5):
                dist = np.abs(normalized_x[i] - self.modal_centers[i, j])
                modal_sum += self.modal_weights[j, i] * (np.exp(-dist**2 / 0.05) + 0.4 * np.sin(3 * dist) + 0.1 * np.cos(7 * dist))
            modal_values[i] = modal_sum
            
        # Combine components with chaotic interaction
        fitness = 0.0
        for i in range(self.dim):
            # Add periodic and modal components with chaotic cubic interaction
            component_value = periodic_components[i] + modal_values[i]
            fitness += component_value**2 + 0.3 * component_value**3 + 0.1 * np.sin(4 * component_value)
            
        # Add radial contribution with chaotic scaling
        fitness += radial_component**2 + 0.2 * np.cos(2 * radial_component)
        
        # Add cross-dimension coupling with enhanced chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_strength[i, j] * (
                        np.sin(periodic_components[i]) * np.cos(periodic_components[j]) + 
                        0.4 * np.sin(periodic_components[i]) * np.sin(periodic_components[j]) +
                        0.2 * np.cos(periodic_components[i]) * np.sin(periodic_components[j])
                    )
                    
        # Add final chaotic scaling and noise
        return fitness + 0.3 * coupling_term + 0.1 * np.sum(np.sin(3.0 * x)**2 + 0.05 * np.cos(7.0 * x))