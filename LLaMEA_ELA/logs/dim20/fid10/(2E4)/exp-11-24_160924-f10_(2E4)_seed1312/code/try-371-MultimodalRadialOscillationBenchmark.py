import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.rbf_weights = np.random.uniform(0.5, 2.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, (dim, dim))
        # Initialize sinusoidal oscillation parameters
        self.osc_freq = np.random.uniform(1.0, 6.0, dim)
        self.osc_amp = np.random.uniform(0.3, 1.5, dim)
        self.osc_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize polynomial interaction coefficients
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, (dim, dim, dim))
        # Initialize cross-dimensional coupling terms with stronger interactions
        self.coupling_strengths = np.random.uniform(0.3, 1.5, (dim, dim))
        # Add additional high-frequency sinusoidal components for increased complexity
        self.high_freq_coeffs = np.random.uniform(2.0, 5.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Radial basis function components
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                center = self.rbf_centers[i][j]
                weight = self.rbf_weights[i][j]
                width = self.rbf_widths[i][j]
                rbf_sum += weight * np.exp(-0.5 * ((x[j] - center) / width)**2)
            result += rbf_sum
            
        # Sinusoidal oscillation components
        for i in range(self.dim):
            freq = self.osc_freq[i]
            amp = self.osc_amp[i]
            phase = self.osc_phase[i]
            oscillation = amp * np.sin(freq * x[i] + phase)
            result += oscillation
            
        # Add high-frequency sinusoidal components
        for i in range(self.dim):
            freq = self.high_freq_coeffs[i]
            oscillation = 0.5 * np.sin(freq * x[i])
            result += oscillation
            
        # Polynomial interaction terms with modified scaling
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(self.dim):
                for k in range(self.dim):
                    coeff = self.poly_coeffs[i][j][k]
                    poly_sum += coeff * x[j] * x[k]
            result += 0.2 * poly_sum**2
            
        # Cross-dimensional coupling with oscillatory behavior and enhanced strength
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    strength = self.coupling_strengths[i][j]
                    coupling_sum += strength * np.sin(x[i] - x[j])
            result += 0.3 * coupling_sum**2
            
        # Add a global polynomial scaling term with different exponents
        poly_scaling = np.sum(x**4) + 0.3 * np.sum(x**5)
        result += 0.15 * poly_scaling
        
        # Reduce noise magnitude but increase its frequency components for better challenge
        noise = np.random.normal(0, 0.02, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.cos(3 * x[i])
            
        return result