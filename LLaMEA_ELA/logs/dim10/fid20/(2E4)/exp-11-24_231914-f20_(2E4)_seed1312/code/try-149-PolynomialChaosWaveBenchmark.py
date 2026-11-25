import numpy as np

class PolynomialChaosWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for polynomial chaos expansion with higher degree terms
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, 7))
        # Wave interference parameters with phase shifts
        self.wave_freqs = np.random.uniform(2.0, 15.0, size=dim)
        self.wave_amps = np.random.uniform(0.3, 4.0, size=dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, size=dim)
        # Fractal coupling parameters with chaotic scaling
        self.fractal_dims = np.random.uniform(0.1, 3.0, size=dim)
        # Stochastic perturbation strength with temporal correlation
        self.stdev = 0.05 + 0.3 * np.random.rand()
        self.correlation = 0.7 + 0.2 * np.random.rand()
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with higher degree terms and cross-terms
        poly_chaos = 0.0
        for i in range(self.dim):
            coeffs = self.poly_coeffs[i]
            xi = x[i]
            # Sum of polynomial terms with random coefficients
            poly_chaos += coeffs[0] + coeffs[1]*xi + coeffs[2]*xi**2 + coeffs[3]*xi**3 + \
                         coeffs[4]*xi**4 + coeffs[5]*xi**5 + coeffs[6]*xi**6
            
        # Trigonometric wave interference component with phase shifts
        wave_interference = 0.0
        for i in range(self.dim):
            freq = self.wave_freqs[i]
            amp = self.wave_amps[i]
            phase = self.wave_phases[i]
            wave_interference += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            
        # Fractal-like coupling with chaotic dimension scaling and cross-dimensional interactions
        fractal_coupling = 0.0
        for i in range(self.dim - 1):
            # Use fractional dimension scaling for fractal behavior
            dim_scaling = self.fractal_dims[i] * self.fractal_dims[i+1]
            fractal_coupling += np.exp(-0.3 * (x[i]**2 + x[i+1]**2)) * \
                               np.sin(dim_scaling * (x[i] + x[i+1])) * \
                               np.cos(0.5 * dim_scaling * (x[i] - x[i+1]))
            
        # Stochastic perturbation component with temporal correlation
        stochastic = 0.0
        prev_noise = np.random.normal(0, self.stdev)
        for i in range(self.dim):
            # Add correlated noise with temporal dependency
            current_noise = self.correlation * prev_noise + (1 - self.correlation) * np.random.normal(0, self.stdev)
            stochastic += current_noise * np.exp(-0.2 * x[i]**2)
            prev_noise = current_noise
            
        # Combined landscape with weighted components
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Enhanced multi-modal structure using product of trigonometric functions with chaotic behavior
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima through chaotic trigonometric products
            multimodal += np.sin(8 * x[i]) * np.cos(5 * x[i]) * np.sin(12 * x[i]) * np.cos(7 * x[i])
            
        # Dimensionality-dependent complexity scaling with exponential growth
        complexity_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * self.dim**1.5
        
        # Add chaotic coupling between dimensions
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Final objective function combining all components
        result = base + complexity_factor * (poly_chaos + wave_interference + 
                                           fractal_coupling + stochastic + multimodal + chaotic_coupling)
        
        return result