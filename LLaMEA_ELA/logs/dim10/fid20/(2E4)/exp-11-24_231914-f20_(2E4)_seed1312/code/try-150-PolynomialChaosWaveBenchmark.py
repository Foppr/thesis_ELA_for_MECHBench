import numpy as np

class PolynomialChaosWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for polynomial chaos expansion with higher degrees
        self.poly_coeffs = np.random.uniform(0.1, 3.0, size=(dim, 7))
        # Wave interference parameters with phase shifts
        self.wave_freqs = np.random.uniform(2.0, 15.0, size=dim)
        self.wave_amps = np.random.uniform(1.0, 4.0, size=dim)
        self.wave_phases = np.random.uniform(0, 2*np.pi, size=dim)
        # Fractal coupling parameters with memory effects
        self.fractal_dims = np.random.uniform(0.3, 2.5, size=dim)
        self.fractal_memory = np.random.rand(dim)
        # Hyperchaotic component parameters
        self.hyperchaos_params = np.random.uniform(0.5, 3.0, size=(dim, 3))
        # Stochastic perturbation strength with time-varying component
        self.stdev = 0.15 + 0.3 * np.random.rand()
        self.time_varying_factor = 0.5 + 0.5 * np.random.rand()
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos component with higher degree terms
        poly_chaos = 0.0
        for i in range(self.dim):
            coeffs = self.poly_coeffs[i]
            xi = x[i]
            # Sum of polynomial terms with random coefficients
            poly_chaos += coeffs[0] + coeffs[1]*xi + coeffs[2]*xi**2 + coeffs[3]*xi**3 + \
                         coeffs[4]*xi**4 + coeffs[5]*xi**5 + coeffs[6]*xi**6
            
        # Trigonometric wave interference with phase shifts
        wave_interference = 0.0
        for i in range(self.dim):
            freq = self.wave_freqs[i]
            amp = self.wave_amps[i]
            phase = self.wave_phases[i]
            wave_interference += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
            
        # Fractal-like coupling with memory and dimension-dependent scaling
        fractal_coupling = 0.0
        for i in range(self.dim - 1):
            dim_scaling = self.fractal_dims[i] + self.fractal_dims[i+1]
            memory_factor = self.fractal_memory[i] * self.fractal_memory[i+1]
            fractal_coupling += np.exp(-0.5 * (x[i]**2 + x[i+1]**2)) * \
                               np.sin(dim_scaling * (x[i] + x[i+1])) * \
                               memory_factor
            
        # Hyperchaotic component for increased complexity
        hyperchaos = 0.0
        for i in range(self.dim):
            a, b, c = self.hyperchaos_params[i]
            # Lorenz-like hyperchaotic system components
            hyperchaos += np.sin(a * x[i]) * np.cos(b * x[i]) * np.exp(-c * x[i]**2)
            
        # Stochastic perturbation component with time-varying influence
        stochastic = 0.0
        for i in range(self.dim):
            # Add normally distributed random noise scaled by stdev and time factor
            noise = np.random.normal(0, self.stdev) * self.time_varying_factor
            stochastic += noise * np.exp(-0.1 * x[i]**2)
            
        # Combined landscape with weighted components
        # Base quadratic term for conditioning
        base = np.sum(x**2) / self.dim
        
        # Enhanced multi-modal structure using product of trigonometric functions with multiple frequencies
        multimodal = 0.0
        for i in range(self.dim):
            # Create multiple local minima through complex trigonometric products
            multimodal += (np.sin(5 * x[i]) * np.cos(3 * x[i]) * np.sin(7 * x[i]) * 
                          np.cos(2 * x[i]) * np.sin(9 * x[i]))
            
        # Dimensionality-dependent complexity scaling with exponential factor
        complexity_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.05 * np.exp(self.dim / 10.0)
        
        # Final objective function combining all components
        result = base + complexity_factor * (poly_chaos + wave_interference + 
                                           fractal_coupling + stochastic + multimodal + hyperchaos)
        
        return result