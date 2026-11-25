import numpy as np

class PolynomialChaosWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for polynomial chaos expansion
        self.poly_coeffs = np.random.uniform(0.1, 2.0, size=(dim, 5))
        # Wave interference parameters
        self.wave_freqs = np.random.uniform(1.0, 15.0, size=dim)
        self.wave_amps = np.random.uniform(0.5, 4.0, size=dim)
        # Fractal coupling parameters
        self.fractal_dims = np.random.uniform(0.3, 2.5, size=dim)
        # Stochastic perturbation strength
        self.stdev = 0.1 + 0.3 * np.random.rand()
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with varying degrees
        poly_chaos = 0.0
        for i in range(self.dim):
            coeffs = self.poly_coeffs[i]
            xi = x[i]
            # Sum of polynomial terms with random coefficients
            poly_chaos += coeffs[0] + coeffs[1]*xi + coeffs[2]*xi**2 + coeffs[3]*xi**3 + coeffs[4]*xi**4
            
        # Trigonometric wave interference component
        wave_interference = 0.0
        for i in range(self.dim):
            freq = self.wave_freqs[i]
            amp = self.wave_amps[i]
            wave_interference += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Fractal-like coupling with dimension-dependent scaling
        fractal_coupling = 0.0
        for i in range(self.dim - 1):
            # Use fractional dimension scaling for fractal behavior
            dim_scaling = self.fractal_dims[i] + self.fractal_dims[i+1]
            fractal_coupling += np.exp(-0.5 * (x[i]**2 + x[i+1]**2)) * \
                               np.sin(dim_scaling * (x[i] + x[i+1]))
            
        # Stochastic perturbation component
        stochastic = 0.0
        for i in range(self.dim):
            # Add normally distributed random noise scaled by stdev
            stochastic += np.random.normal(0, self.stdev) * np.exp(-0.1 * x[i]**2)
            
        # Combined landscape with weighted components
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Enhanced multi-modal structure using product of trigonometric functions
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima through trigonometric products
            multimodal += np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.sin(7 * x[i]) * np.cos(2 * x[i])
            
        # Dimensionality-dependent complexity scaling
        complexity_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Add a new component for enhanced ruggedness and nonlinearity
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += np.sin(10 * x[i]) * np.cos(8 * x[i]) * np.tan(0.5 * x[i])
            
        # Final objective function combining all components
        result = base + complexity_factor * (poly_chaos + wave_interference + 
                                           fractal_coupling + stochastic + multimodal + ruggedness)
        
        return result