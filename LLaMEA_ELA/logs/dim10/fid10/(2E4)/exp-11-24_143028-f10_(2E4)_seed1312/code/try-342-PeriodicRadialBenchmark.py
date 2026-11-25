import numpy as np

class PeriodicRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced periodic parameters with higher frequency range and amplitude modulation
        self.frequencies = np.random.uniform(2.0, 10.0, dim)
        self.amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Radial parameters with increased complexity
        self.radial_freq = np.random.uniform(1.0, 6.0, dim)
        self.radial_amp = np.random.uniform(0.5, 2.0, dim)
        # Stronger conditioning and added chaos
        self.conditioning = np.random.uniform(0.5, 15.0, dim)
        # Multi-modal structure with increased number of centers and chaotic shifts
        self.modal_centers = np.random.uniform(-4.5, 4.5, (dim, 6)) + np.random.randn(dim, 6) * 0.5
        self.modal_weights = np.random.dirichlet(np.ones(6), dim).T
        # Cross-dimension coupling with chaotic interaction patterns
        self.coupling_strength = np.random.uniform(0.8, 1.5, (dim, dim))
        np.fill_diagonal(self.coupling_strength, 0.0)
        # Chaotic attractor inspired term
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for periodic components
        normalized_x = x / 5.0
        
        # Compute radial component with enhanced nonlinearity
        r = np.sqrt(np.sum(normalized_x**2))
        radial_component = np.sum(self.radial_amp * np.sin(self.radial_freq * r) * np.cos(self.radial_freq * r))
        
        # Compute periodic components with higher-order harmonics and chaotic modulation
        periodic_components = np.zeros(self.dim)
        for i in range(self.dim):
            base_term = self.amplitudes[i] * np.sin(
                self.frequencies[i] * normalized_x[i] + self.phases[i]
            )
            harmonic_2 = 0.3 * np.sin(2 * self.frequencies[i] * normalized_x[i])
            harmonic_3 = 0.2 * np.sin(3 * self.frequencies[i] * normalized_x[i])
            chaotic_mod = np.sin(self.chaotic_params[i] * r)
            periodic_components[i] = (base_term + harmonic_2 + harmonic_3) * self.conditioning[i] * chaotic_mod
            
        # Multi-modal structure with enhanced cubic response and additional noise
        modal_values = np.zeros(self.dim)
        for i in range(self.dim):
            modal_sum = 0.0
            for j in range(6):
                dist = np.abs(normalized_x[i] - self.modal_centers[i, j])
                # Add chaotic perturbation to modal distances
                perturb = 0.1 * np.sin(5 * dist + self.phases[i])
                modal_sum += self.modal_weights[j, i] * np.exp(-dist**2 / 0.1) + 0.3 * np.sin(3 * dist) + perturb
            modal_values[i] = modal_sum
            
        # Combine components with enhanced nonlinear interactions
        fitness = 0.0
        for i in range(self.dim):
            component_value = periodic_components[i] + modal_values[i]
            # Add higher-order polynomial terms and chaotic feedback
            fitness += component_value**2 + 0.3 * component_value**3 + 0.1 * component_value**4
            
        # Add radial contribution with chaotic interaction
        fitness += radial_component**2 + 0.2 * np.sin(5 * r) * radial_component
        
        # Enhanced cross-dimension coupling with chaotic interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_interaction = (
                        np.sin(periodic_components[i]) * np.cos(periodic_components[j]) + 
                        0.5 * np.sin(2 * periodic_components[i]) * np.sin(periodic_components[j]) +
                        0.3 * np.cos(periodic_components[i]) * np.sin(2 * periodic_components[j])
                    )
                    coupling_term += self.coupling_strength[i, j] * coupling_interaction
                    
        # Add chaotic attractor term
        chaotic_attractor = 0.0
        for i in range(self.dim):
            chaotic_attractor += np.sin(self.chaotic_params[i] * x[i]) * np.cos(self.chaotic_params[i] * x[(i+1)%self.dim])
            
        # Final scaling and noise with chaotic feedback
        return fitness + 0.5 * coupling_term + 0.2 * chaotic_attractor + 0.1 * np.sum(np.sin(3.0 * x)**3)