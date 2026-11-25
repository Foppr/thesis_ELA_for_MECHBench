import numpy as np

class MultimodalRadialOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for radial basis functions with modified structure
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (dim, dim))
        self.rbf_weights = np.random.uniform(0.5, 2.0, (dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.5, (dim, dim))
        # Initialize enhanced sinusoidal oscillation parameters
        self.osc_freq = np.random.uniform(1.5, 7.0, dim)
        self.osc_amp = np.random.uniform(0.4, 1.8, dim)
        self.osc_phase = np.random.uniform(0.0, 2*np.pi, dim)
        # Initialize polynomial interaction coefficients with higher-order terms
        self.poly_coeffs = np.random.uniform(-0.3, 0.3, (dim, dim, dim))
        # Initialize cross-dimensional coupling terms with different structure
        self.coupling_strengths = np.random.uniform(0.2, 1.5, (dim, dim))
        # Add additional harmonic components for complexity
        self.harmonic_freq = np.random.uniform(0.5, 3.0, dim)
        self.harmonic_amp = np.random.uniform(0.1, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced radial basis function components
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                center = self.rbf_centers[i][j]
                weight = self.rbf_weights[i][j]
                width = self.rbf_widths[i][j]
                # Modified RBF with additional exponential scaling
                rbf_sum += weight * np.exp(-0.5 * ((x[j] - center) / width)**2) * (1.0 + 0.1 * np.sin(0.5 * x[j]))
            result += rbf_sum
            
        # Enhanced sinusoidal oscillation components with harmonic additions
        for i in range(self.dim):
            freq = self.osc_freq[i]
            amp = self.osc_amp[i]
            phase = self.osc_phase[i]
            oscillation = amp * np.sin(freq * x[i] + phase)
            # Add harmonic component for increased complexity
            harmonic = self.harmonic_amp[i] * np.sin(self.harmonic_freq[i] * x[i] + phase)
            result += oscillation + 0.5 * harmonic
            
        # Enhanced polynomial interaction terms with cubic components
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(self.dim):
                for k in range(self.dim):
                    coeff = self.poly_coeffs[i][j][k]
                    poly_sum += coeff * x[j] * x[k]
            # Add cubic term for increased nonlinearity
            result += 0.15 * poly_sum**3
            
        # Modified cross-dimensional coupling with enhanced oscillatory behavior
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    strength = self.coupling_strengths[i][j]
                    # Enhanced coupling with additional sinusoidal modulation
                    coupling_sum += strength * np.sin(x[i] - x[j]) * (1.0 + 0.2 * np.cos(0.3 * x[i]))
            result += 0.25 * coupling_sum**2
            
        # Add global polynomial scaling term with higher-order components
        poly_scaling = np.sum(x**4) + 0.3 * np.sum(x**5)
        result += 0.12 * poly_scaling
        
        # Reduced noise level for improved consistency
        noise = np.random.normal(0, 0.02, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.cos(3 * x[i])
            
        return result