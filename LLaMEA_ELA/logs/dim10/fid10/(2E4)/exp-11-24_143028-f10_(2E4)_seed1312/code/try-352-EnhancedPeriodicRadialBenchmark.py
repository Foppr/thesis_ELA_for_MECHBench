import numpy as np

class EnhancedPeriodicRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize periodic parameters with chaotic frequency distribution
        self.frequencies = np.random.uniform(2.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.3, 2.5, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Radial parameters with fractal-like scaling
        self.radial_freq = np.random.uniform(1.0, 5.0, dim)
        self.radial_amp = np.random.uniform(0.2, 1.5, dim)
        # Conditioning parameters with quantum-inspired distribution
        self.conditioning = np.power(10.0, np.random.uniform(-1.0, 2.0, dim))
        # Multi-modal structure with fractal-like centers and quantum weights
        self.modal_centers = np.random.uniform(-4.0, 4.0, (dim, 5))  # Increased number of modes
        self.modal_weights = np.random.dirichlet(np.ones(5), dim).T
        # Cross-dimension coupling with chaotic strength and quantum interaction
        self.coupling_strength = np.random.uniform(0.5, 1.2, (dim, dim))
        np.fill_diagonal(self.coupling_strength, 0.0)
        # Quantum-inspired noise parameters
        self.noise_amplitude = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for periodic components
        normalized_x = x / 5.0
        
        # Compute radial component with fractal-like scaling
        r = np.sqrt(np.sum(normalized_x**2))
        radial_component = np.sum(self.radial_amp * np.sin(self.radial_freq * r) * np.cos(r * 3.0))
        
        # Compute periodic components with chaotic cubic nonlinearities
        periodic_components = np.zeros(self.dim)
        for i in range(self.dim):
            # Base periodic term with chaotic cubic modulation
            base_term = self.amplitudes[i] * np.sin(
                self.frequencies[i] * normalized_x[i] + self.phases[i]
            )
            cubic_term = 0.6 * np.sin(3 * self.frequencies[i] * normalized_x[i]) + \
                        0.2 * np.sin(5 * self.frequencies[i] * normalized_x[i])
            periodic_components[i] = (base_term + cubic_term) * self.conditioning[i]
            
        # Multi-modal structure with fractal-like response
        modal_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Weighted sum of modal contributions with fractal scaling
            modal_sum = 0.0
            for j in range(5):
                dist = np.abs(normalized_x[i] - self.modal_centers[i, j])
                # Fractal-like weighting with quantum-inspired scaling
                weight = self.modal_weights[j, i] * np.exp(-dist**2 / 0.05) + \
                        0.1 * np.sin(3 * dist) * np.cos(dist)
                modal_sum += weight
            modal_values[i] = modal_sum
            
        # Combine components with quantum-inspired energy landscape
        fitness = 0.0
        for i in range(self.dim):
            # Add periodic and modal components with chaotic interaction
            component_value = periodic_components[i] + modal_values[i]
            # Quantum-inspired cubic and quartic terms
            fitness += component_value**2 + 0.2 * component_value**3 + 0.05 * component_value**4
            
        # Add radial contribution with quantum scaling
        fitness += radial_component**2
        
        # Add cross-dimension coupling with chaotic nonlinear interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Quantum-inspired coupling with chaotic phase interaction
                    phase_diff = np.sin(periodic_components[i]) * np.cos(periodic_components[j])
                    coupling_term += self.coupling_strength[i, j] * (
                        phase_diff + 0.2 * np.sin(phase_diff) * np.cos(phase_diff)
                    )
                    
        # Add quantum-inspired noise and final scaling
        quantum_noise = np.sum(self.noise_amplitude * np.sin(10.0 * x))
        return fitness + 0.3 * coupling_term + quantum_noise + 0.1 * np.sum(np.sin(3.0 * x)**2)