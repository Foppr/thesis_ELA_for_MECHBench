import numpy as np

class PolynomialChaosEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos structure parameters
        self.poly_orders = np.random.randint(3, 8, dim)
        self.elliptic_axes = np.random.uniform(0.5, 3.0, dim)
        self.harmonic_frequencies = np.random.uniform(1.0, 6.0, dim)
        # Adaptive elliptic sections
        self.ellipse_centers = np.random.uniform(-2.0, 2.0, dim)
        self.ellipse_radii = np.random.uniform(1.0, 4.0, dim)
        # Cross-dimensional harmonic coupling
        self.coupling_weights = np.random.uniform(0.3, 1.5, (dim, dim))
        # Dynamic conditioning gradients
        self.conditioning_gradients = np.random.uniform(0.1, 2.0, dim)
        # Chaos modulation parameters
        self.chaos_amplitude = 0.8 + np.random.rand() * 0.7
        self.chaos_frequency = 0.5 + np.random.rand() * 1.5
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Polynomial chaos terms with adaptive orders
        poly_term = 0.0
        for i in range(self.dim):
            order = self.poly_orders[i]
            center = self.ellipse_centers[i]
            radius = self.ellipse_radii[i]
            # Polynomial chaos with elliptic geometry
            distance = (x_norm[i] - center) / radius
            poly_val = np.abs(distance) ** order
            poly_term += poly_val
            
        # Elliptic section terms with adaptive axes
        ellipse_term = 0.0
        for i in range(self.dim):
            axis = self.elliptic_axes[i]
            center = self.ellipse_centers[i]
            radius = self.ellipse_radii[i]
            # Elliptic harmonic pattern
            angle = np.arctan2(x_norm[i] - center, 1.0) * axis
            ellipse_val = (x_norm[i] - center) ** 2 / (radius ** 2) + 0.5 * np.sin(angle)
            ellipse_term += ellipse_val
            
        # Harmonic coupling between dimensions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                weight = self.coupling_weights[i, j]
                freq_i = self.harmonic_frequencies[i]
                freq_j = self.harmonic_frequencies[j]
                # Cross-dimensional harmonic interaction
                coupling_val = weight * np.sin(freq_i * x_norm[i]) * np.cos(freq_j * x_norm[j])
                coupling_term += coupling_val
                
        # Dynamic conditioning with gradient modulation
        cond_term = 0.0
        for i in range(self.dim):
            grad = self.conditioning_gradients[i]
            freq = self.harmonic_frequencies[i]
            # Gradient-based conditioning with harmonic modulation
            cond_val = grad * np.exp(0.5 * x_norm[i] ** 2) * (1.0 + 0.3 * np.sin(freq * x_norm[i]))
            cond_term += cond_val
            
        # Chaos modulation term
        chaos_term = 0.0
        for i in range(self.dim):
            amplitude = self.chaos_amplitude
            frequency = self.chaos_frequency
            # Chaotic oscillation with dynamic frequency
            chaos_val = amplitude * np.sin(frequency * x_norm[i] + np.cos(x_norm[i]))
            chaos_term += chaos_val
            
        # Combined function with weighted components
        result = 1.5 * poly_term + 1.2 * ellipse_term + 0.8 * coupling_term + 1.0 * cond_term + 0.5 * chaos_term
        
        # Add noise with polynomial characteristics
        noise_amplitude = 0.03 * (1.0 + 0.1 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise