import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for radial basis functions with modified weights and widths
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.rbf_weights = np.random.uniform(1.0, 3.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.3, 1.8, (dim, dim))
        # Initialize sinusoidal oscillation parameters with higher frequencies
        self.osc_freq = np.random.uniform(2.0, 8.0, dim)
        self.osc_amp = np.random.uniform(0.5, 2.0, dim)
        self.osc_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize polynomial interaction coefficients with higher magnitudes
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, dim, dim))
        # Initialize cross-dimensional coupling terms with stronger interactions
        self.coupling_strengths = np.random.uniform(0.5, 2.0, (dim, dim))
        
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
            
        # Polynomial interaction terms with higher-order coupling
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(self.dim):
                for k in range(self.dim):
                    coeff = self.poly_coeffs[i][j][k]
                    poly_sum += coeff * x[j] * x[k]
            result += 0.2 * poly_sum**2
            
        # Cross-dimensional coupling with enhanced oscillatory behavior
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    strength = self.coupling_strengths[i][j]
                    coupling_sum += strength * np.sin(2 * (x[i] - x[j]))
            result += 0.3 * coupling_sum**2
            
        # Add a global polynomial scaling term with higher-order terms
        poly_scaling = np.sum(x**4) + 0.7 * np.sum(x**5)
        result += 0.15 * poly_scaling
        
        # Add noise for increased complexity
        noise = np.random.normal(0, 0.08, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.cos(3 * x[i])
            
        return result