import numpy as np

class PeriodicRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize periodic parameters
        self.frequencies = np.random.uniform(1.5, 7.0, dim)
        self.amplitudes = np.random.uniform(0.6, 2.5, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Radial parameters
        self.radial_freq = np.random.uniform(0.8, 4.0, dim)
        self.radial_amp = np.random.uniform(0.2, 1.5, dim)
        # Conditioning parameters
        self.conditioning = np.random.uniform(0.2, 12.0, dim)
        # Multi-modal structure with shifted centers
        self.modal_centers = np.random.uniform(-4.0, 4.0, (dim, 4)) + 1.5  # Increased shift
        self.modal_weights = np.random.dirichlet(np.ones(4), dim).T
        # Cross-dimension coupling - increased strength and modified interaction
        self.coupling_strength = np.random.uniform(0.7, 1.2, (dim, dim))
        np.fill_diagonal(self.coupling_strength, 0.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for periodic components
        normalized_x = x / 5.0
        
        # Compute radial component
        r = np.sqrt(np.sum(normalized_x**2))
        radial_component = np.sum(self.radial_amp * np.sin(self.radial_freq * r))
        
        # Compute periodic components with cubic nonlinearities
        periodic_components = np.zeros(self.dim)
        for i in range(self.dim):
            # Base periodic term with cubic modulation
            base_term = self.amplitudes[i] * np.sin(
                self.frequencies[i] * normalized_x[i] + self.phases[i]
            )
            cubic_term = 0.6 * np.sin(3 * self.frequencies[i] * normalized_x[i])
            periodic_components[i] = (base_term + cubic_term) * self.conditioning[i]
            
        # Multi-modal structure
        modal_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Weighted sum of modal contributions with cubic response
            modal_sum = 0.0
            for j in range(4):
                dist = np.abs(normalized_x[i] - self.modal_centers[i, j])
                modal_sum += self.modal_weights[j, i] * np.exp(-dist**2 / 0.15) + 0.5 * np.sin(2 * dist)
            modal_values[i] = modal_sum
            
        # Combine components
        fitness = 0.0
        for i in range(self.dim):
            # Add periodic and modal components with cubic interaction
            component_value = periodic_components[i] + modal_values[i]
            fitness += component_value**2 + 0.3 * component_value**3  # Increased cubic term
            
        # Add radial contribution
        fitness += radial_component**2
        
        # Add cross-dimension coupling with enhanced nonlinear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_strength[i, j] * (
                        np.sin(periodic_components[i]) * np.cos(periodic_components[j]) + 
                        0.5 * np.sin(periodic_components[i]) * np.sin(periodic_components[j])
                    )
                    
        # Add final scaling and noise
        return fitness + 0.4 * coupling_term + 0.1 * np.sum(np.sin(2.0 * x)**2)