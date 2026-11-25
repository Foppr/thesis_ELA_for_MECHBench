import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute highly chaotic parameters with fractal scaling
        self.freqs = np.random.uniform(5.0, 25.0, dim)
        self.amps = np.random.uniform(1.0, 5.0, dim)
        self.phase_shifts = np.random.uniform(0, 4*np.pi, dim)
        self.radial_freq = np.random.uniform(3.0, 10.0)
        self.coupling_strength = 0.7
        # Fractal dimension scaling factor with modified sensitivity
        self.fractal_dim = 1.0 + 0.7 * np.sin(dim * 0.4)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Fractal radial component with multi-scale chaotic oscillations
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = self.radial_freq * r * np.sin(self.radial_freq * r) * np.cos(self.radial_freq * r**3)
        
        # Multi-scale chaotic gradient with fractal modulation
        gradient = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            amp = self.amps[i]
            phase = self.phase_shifts[i]
            
            # Multi-scale sinusoidal modulation with enhanced nonlinearity
            modulator = (np.sin(freq * x_scaled[i] + phase) + 
                        0.3 * np.cos(2 * freq * x_scaled[i] + phase) +
                        0.1 * np.sin(3 * freq * x_scaled[i] + phase) +
                        0.05 * np.sin(5 * freq * x_scaled[i] + phase))
            gradient += amp * x_scaled[i] * modulator
        
        # Fractal cross-dimensional coupling with adaptive strength and modified interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Adaptive chaotic coupling based on fractal dimension with increased complexity
                coupling_strength = self.coupling_strength * (1.0 + 0.3 * np.sin(self.fractal_dim * i * j))
                coupling_term = np.sin(self.freqs[i] * x_scaled[i] + self.freqs[j] * x_scaled[j]) * \
                              np.cos(0.5 * (self.freqs[i] + self.freqs[j]) * (x_scaled[i] - x_scaled[j]))
                coupling += coupling_term * np.exp(-0.2 * (x_scaled[i]**2 + x_scaled[j]**2)) * coupling_strength
        
        # Fractal radial decay with multi-frequency oscillation and enhanced nonlinearity
        radial_decay = np.exp(-r**4) * np.sin(6 * r) * np.cos(3 * r**2)
        
        # Multi-scale fractal chaotic structure with increased complexity
        chaotic_structure = 0.0
        for i in range(self.dim):
            # Multiple chaotic frequencies with fractal scaling and additional harmonic components
            freqs = [self.freqs[i], self.freqs[i]*1.3, self.freqs[i]*1.7, self.freqs[i]*2.3, self.freqs[i]*3.1]
            for f in freqs:
                chaotic_structure += np.sin(f * x_scaled[i]) * np.cos(f * x_scaled[i]**3) * np.exp(-0.15 * f)
        
        # Fractal dimension-dependent scaling with modified sensitivity
        dim_scaling = 1.0 + 0.15 * (self.dim - 2) * self.fractal_dim
        
        # Combine all components with fractal weighting and increased complexity
        result = (gradient**2 * dim_scaling + 
                 0.8 * radial_term + 
                 self.coupling_strength * coupling + 
                 0.6 * radial_decay + 
                 0.5 * chaotic_structure)
        
        # Adaptive noise based on fractal dimension and problem complexity
        noise_amp = 0.03 * (1.0 + 0.15 * np.sin(self.fractal_dim * self.dim))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise