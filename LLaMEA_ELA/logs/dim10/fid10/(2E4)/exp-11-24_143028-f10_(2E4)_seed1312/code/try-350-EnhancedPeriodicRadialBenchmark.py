import numpy as np

class EnhancedPeriodicRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic periodic parameters with fractal characteristics
        self.frequencies = 2.0 + 4.0 * np.sin(np.arange(dim) * np.pi / (dim + 1))
        self.amplitudes = 1.5 + 1.5 * np.cos(np.arange(dim) * np.pi / (dim + 1))
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Radial parameters with exponential scaling
        self.radial_freq = np.exp(np.random.uniform(0.5, 2.0, dim))
        self.radial_amp = np.random.uniform(0.5, 2.0, dim)
        # Extreme conditioning with power-law distribution
        self.conditioning = np.power(np.random.uniform(0.1, 10.0, dim), 1.5)
        # Multi-modal structure with quantum-like superposition
        self.modal_centers = np.random.uniform(-4.0, 4.0, (dim, 5))  # More centers
        self.modal_weights = np.random.dirichlet(np.ones(5), dim).T
        # Cross-dimension coupling with chaotic interaction matrix
        self.coupling_strength = np.zeros((dim, dim))
        for i in range(dim):
            for j in range(dim):
                if i != j:
                    self.coupling_strength[i, j] = np.sin(i * j) * np.cos(i + j) * np.random.uniform(0.5, 1.5)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for periodic components
        normalized_x = x / 5.0
        
        # Compute radial component with fractal scaling
        r = np.sqrt(np.sum(normalized_x**2))
        radial_component = np.sum(self.radial_amp * np.sin(self.radial_freq * r**1.7))  # Nonlinear radial
        
        # Compute periodic components with quantum-like interference
        periodic_components = np.zeros(self.dim)
        for i in range(self.dim):
            base_term = self.amplitudes[i] * np.sin(
                self.frequencies[i] * normalized_x[i] + self.phases[i]
            )
            # Add quantum interference terms
            interference = 0.3 * np.sin(2 * self.frequencies[i] * normalized_x[i]) * np.cos(3 * self.frequencies[i] * normalized_x[i])
            periodic_components[i] = (base_term + interference) * self.conditioning[i]
            
        # Multi-modal structure with fractal scaling
        modal_values = np.zeros(self.dim)
        for i in range(self.dim):
            modal_sum = 0.0
            for j in range(5):
                dist = np.abs(normalized_x[i] - self.modal_centers[i, j])
                # Fractal-like response with multiple scales
                modal_sum += self.modal_weights[j, i] * (
                    np.exp(-dist**2 / 0.05) + 
                    0.2 * np.sin(10 * dist) * np.exp(-dist**2 / 0.2)
                )
            modal_values[i] = modal_sum
            
        # Combine components with chaotic energy landscape
        fitness = 0.0
        for i in range(self.dim):
            component_value = periodic_components[i] + modal_values[i]
            # Add chaotic cubic and quartic terms
            fitness += component_value**2 + 0.2 * component_value**3 + 0.05 * component_value**4
            
        # Add radial contribution with chaotic scaling
        fitness += 0.5 * radial_component**2 + 0.1 * radial_component**3
        
        # Add cross-dimension coupling with quantum interference
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_strength[i, j] * (
                        np.sin(periodic_components[i]) * np.cos(periodic_components[j]) + 
                        0.5 * np.sin(2 * periodic_components[i]) * np.sin(2 * periodic_components[j]) +
                        0.3 * np.cos(periodic_components[i]) * np.sin(periodic_components[j])
                    )
                    
        # Add final chaotic scaling and noise
        return fitness + 0.3 * coupling_term + 0.1 * np.sum(np.sin(3.0 * x)**2) + 0.05 * np.random.rand()