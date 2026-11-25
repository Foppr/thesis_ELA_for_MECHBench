import numpy as np

class QuantumFractalRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = np.random.uniform(0.5, 3.0, size=dim)
        self.phi = np.random.uniform(0, 2*np.pi, size=dim)
        self.amplitude = np.random.uniform(0.5, 2.0, size=dim)
        
        # Fractal Brownian motion parameters
        self.hurst = np.random.uniform(0.1, 0.9, size=dim)
        self.fractal_scale = np.random.uniform(0.1, 2.0, size=dim)
        
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(20, dim))
        self.rbf_widths = np.random.uniform(0.1, 3.0, size=20)
        
        # Dynamic conditioning parameters
        self.conditioning_factor = np.random.uniform(0.1, 10.0, size=dim)
        self.conditioning_shift = np.random.uniform(-1.0, 1.0, size=dim)
        
        # Cross-dimensional coupling strengths
        self.coupling_matrix = np.random.uniform(-0.5, 0.5, size=(dim, dim))
        np.fill_diagonal(self.coupling_matrix, 0)
        
        # Adaptive parameter modulation
        self.adaptation_rate = np.random.uniform(0.01, 0.2, size=dim)
        self.modulation_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Multi-scale frequency components
        self.freq_scales = np.random.uniform(0.1, 5.0, size=dim)
        self.freq_amplitudes = np.random.uniform(0.1, 3.0, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        quantum_component = 0.0
        for i in range(self.dim):
            quantum_val = self.amplitude[i] * np.sin(self.omega[i] * x[i] + self.phi[i])
            quantum_component += quantum_val
            
        # Fractal Brownian motion component
        fbm_component = 0.0
        for i in range(self.dim):
            # Simple fractal noise approximation using sine waves
            fbm_val = 0.0
            for k in range(1, 6):
                freq = k * self.freq_scales[i]
                amp = self.fractal_scale[i] / (k ** (2 * self.hurst[i]))
                fbm_val += amp * np.sin(freq * x[i])
            fbm_component += fbm_val
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(20):
            dist = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_val = self.rbf_widths[i] * np.exp(-dist / (2 * self.rbf_widths[i]**2))
            rbf_component += rbf_val
            
        # Dynamic conditioning component
        condition_component = 0.0
        for i in range(self.dim):
            cond_val = self.conditioning_factor[i] * (x[i] + self.conditioning_shift[i])**2
            condition_component += cond_val
            
        # Cross-dimensional coupling component
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_matrix[i, j] * x[i] * x[j]
                    
        # Adaptive modulation component
        adapt_component = 0.0
        for i in range(self.dim):
            adapt_val = np.sin(self.adaptation_rate[i] * x[i] + self.modulation_phase[i])
            adapt_component += adapt_val
            
        # Multi-scale frequency component
        freq_component = 0.0
        for i in range(self.dim):
            freq_val = 0.0
            for k in range(1, 8):
                freq_val += self.freq_amplitudes[i] * np.sin(k * self.freq_scales[i] * x[i])
            freq_component += freq_val
            
        # Combine all components with appropriate weights
        return (1.5 * quantum_component + 
                1.3 * fbm_component + 
                1.2 * rbf_component + 
                1.4 * condition_component + 
                0.8 * coupling_component + 
                0.6 * adapt_component + 
                0.7 * freq_component)