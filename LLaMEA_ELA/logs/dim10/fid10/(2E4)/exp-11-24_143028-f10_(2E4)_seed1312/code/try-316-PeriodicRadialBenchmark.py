import numpy as np

class PeriodicRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize periodic parameters with slight modifications
        self.frequencies = np.random.uniform(1.5, 7.0, dim)
        self.amplitudes = np.random.uniform(0.8, 2.5, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        # Radial parameters
        self.radial_freq = np.random.uniform(0.8, 4.0, dim)
        self.radial_amp = np.random.uniform(0.2, 1.5, dim)
        # Conditioning parameters - increased variation
        self.conditioning = np.random.uniform(0.2, 15.0, dim)
        # Multi-modal structure - changed to more complex centers and weights
        self.modal_centers = np.random.uniform(-4.0, 4.0, (dim, 4))
        self.modal_weights = np.random.dirichlet(np.ones(4), dim).T
        # Cross-dimension coupling - stronger and more complex
        self.coupling_strength = np.random.uniform(0.2, 0.8, (dim, dim))
        np.fill_diagonal(self.coupling_strength, 0.0)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Normalize to [-1, 1] for periodic components
        normalized_x = x / 5.0
        
        # Compute radial component
        r = np.sqrt(np.sum(normalized_x**2))
        radial_component = np.sum(self.radial_amp * np.sin(self.radial_freq * r))
        
        # Compute periodic components
        periodic_components = np.zeros(self.dim)
        for i in range(self.dim):
            # Base periodic term with modified nonlinearity
            periodic_components[i] = self.amplitudes[i] * np.sin(
                self.frequencies[i] * normalized_x[i] + self.phases[i]
            )
            # Add conditioning with exponential scaling
            periodic_components[i] *= np.exp(self.conditioning[i] * 0.1)
            
        # Multi-modal structure with more complex interaction
        modal_values = np.zeros(self.dim)
        for i in range(self.dim):
            # Weighted sum of modal contributions with different decay
            modal_sum = 0.0
            for j in range(4):
                dist = np.abs(normalized_x[i] - self.modal_centers[i, j])
                modal_sum += self.modal_weights[j, i] * np.exp(-dist**2 / 0.05)
            modal_values[i] = modal_sum
            
        # Combine components
        fitness = 0.0
        for i in range(self.dim):
            # Add periodic and modal components with quadratic interaction
            component_value = periodic_components[i] + modal_values[i]
            fitness += component_value**2
            
        # Add radial contribution with modified amplitude
        fitness += 1.5 * radial_component**2
        
        # Add cross-dimension coupling with trigonometric interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_strength[i, j] * (
                        np.sin(periodic_components[i]) * np.sin(periodic_components[j])
                    )
                    
        # Add final scaling and noise with different coefficients
        return fitness + 0.15 * coupling_term + 0.08 * np.sum(np.cos(3.0 * x)**2)