import numpy as np

class TrigonometricRadialAdaptiveLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize trigonometric components with varying frequencies
        self.trig_frequencies = np.random.uniform(1.0, 10.0, dim)
        self.trig_amplitudes = np.random.uniform(0.5, 2.0, dim)
        # Initialize radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (dim, 5))
        self.rbf_widths = np.random.uniform(0.5, 3.0, 5)
        # Initialize adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 1.0, dim)
        self.noise_frequency = np.random.uniform(0.1, 0.5, dim)
        # Initialize coupling coefficients for inter-dimensional interactions
        self.coupling_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize phase shifts for trigonometric components
        self.phases = np.random.uniform(0, 2*np.pi, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Compute trigonometric components
        trig_terms = 0.0
        for j in range(self.dim):
            trig_term = self.trig_amplitudes[j] * np.sin(self.trig_frequencies[j] * x[j] + self.phases[j])
            trig_terms += trig_term
        
        # Compute radial basis function components
        rbf_terms = 0.0
        for i in range(5):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += (x[j] - self.rbf_centers[j, i])**2
            rbf_terms += np.exp(-rbf_sum / (2 * self.rbf_widths[i]**2))
        
        # Compute adaptive noise components
        noise_terms = 0.0
        for j in range(self.dim):
            noise_term = self.noise_amplitude[j] * np.sin(self.noise_frequency[j] * x[j])
            noise_terms += noise_term
        
        # Compute coupling terms between dimensions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += self.coupling_coeffs[i, j] * x[i] * x[j]
        
        # Combine all components with appropriate weights
        total = 0.6 * trig_terms + 0.3 * rbf_terms + 0.2 * noise_terms + 0.4 * coupling_terms
        
        return total