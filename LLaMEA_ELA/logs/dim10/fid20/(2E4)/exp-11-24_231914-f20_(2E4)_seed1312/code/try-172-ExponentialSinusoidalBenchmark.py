import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic sine wave parameters
        self.chaotic_freq = np.random.uniform(2.0, 15.0, size=dim)
        self.chaotic_amp = np.random.uniform(1.0, 4.0, size=dim)
        self.chaotic_phase = np.random.uniform(0, 2*np.pi, size=dim)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, size=(dim, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=dim)
        # Quantum-like interference parameters
        self.interference_strength = np.random.uniform(0.5, 2.5, size=dim)
        self.interference_phase = np.random.uniform(0, 4*np.pi, size=dim)
        # Dynamic conditioning parameters
        self.conditioning = np.random.uniform(0.1, 5.0, size=dim)
        self.conditioning_exponent = np.random.uniform(1.0, 3.0, size=dim)
        # High-order coupling weights
        self.high_order_weights = np.random.uniform(-1.0, 1.0, size=(dim, dim, dim))
        # Fractal-like ruggedness parameters
        self.fractal_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.fractal_amp = np.random.uniform(0.2, 1.5, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with phase modulation
        chaotic_wave = 0.0
        for i in range(self.dim):
            phase_mod = np.sin(self.chaotic_phase[i] + x[(i+1)%self.dim])
            chaotic_wave += (np.sin(self.chaotic_freq[i] * x[i] + phase_mod) * 
                           self.chaotic_amp[i] * np.exp(-0.1 * x[i]**2))
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_sum = 0.0
            for j in range(self.dim):
                rbf_sum += np.exp(-0.5 * ((x[i] - self.rbf_centers[j, i]) / self.rbf_widths[j])**2)
            rbf_component += rbf_sum * self.conditioning[i]
            
        # Quantum-like interference pattern
        quantum_interference = 0.0
        for i in range(self.dim):
            interference_term = np.sin(self.interference_strength[i] * x[i] + self.interference_phase[i])
            quantum_interference += interference_term * np.cos(2 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Dynamic conditioning with power transformation
        conditioning_component = 0.0
        for i in range(self.dim):
            conditioning_component += (x[i]**self.conditioning_exponent[i]) * self.conditioning[i]
            
        # High-order coupling with cubic terms
        high_order_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(self.dim):
                    if i != j and j != k and i != k:
                        high_order_coupling += self.high_order_weights[i, j, k] * x[i]**3 * x[j]**2 * x[k]
                        
        # Fractal-like ruggedness with multiple frequency components
        fractal_ruggedness = 0.0
        for i in range(self.dim):
            base_fractal = (np.sin(self.fractal_freq[i] * x[i]) * 
                          np.cos(self.fractal_freq[i] * x[i] / 3) * 
                          self.fractal_amp[i])
            fractal_ruggedness += base_fractal + 0.5 * np.sin(3 * self.fractal_freq[i] * x[i])
            
        # Combine all components with optimized weights
        return (1.5 * chaotic_wave + 
                1.2 * rbf_component + 
                1.3 * quantum_interference + 
                1.1 * conditioning_component + 
                0.9 * high_order_coupling + 
                0.8 * fractal_ruggedness)