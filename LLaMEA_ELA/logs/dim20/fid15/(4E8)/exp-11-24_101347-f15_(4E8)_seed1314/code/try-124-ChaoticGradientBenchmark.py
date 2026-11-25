import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters
        self.freqs = np.random.uniform(1.0, 10.0, dim)
        self.amps = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.radial_freq = np.random.uniform(0.5, 3.0)
        self.coupling_strength = 0.3
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with chaotic oscillations
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = self.radial_freq * r * np.sin(self.radial_freq * r) * np.cos(self.radial_freq * r**2)
        
        # Chaotic gradient component with sinusoidal modulation
        gradient = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            amp = self.amps[i]
            phase = self.phase_shifts[i]
            
            # Sinusoidal modulation of gradient
            modulator = np.sin(freq * x_scaled[i] + phase) + 0.5 * np.cos(2 * freq * x_scaled[i] + phase)
            gradient += amp * x_scaled[i] * modulator
        
        # Cross-dimensional coupling with chaotic interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Chaotic coupling between dimensions
                coupling_term = np.sin(self.freqs[i] * x_scaled[i] + self.freqs[j] * x_scaled[j])
                coupling += coupling_term * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Radial decay with sinusoidal oscillation
        radial_decay = np.exp(-r**2) * np.sin(3 * r)
        
        # Multi-scale chaotic structure
        chaotic_structure = 0.0
        for i in range(self.dim):
            # Multiple chaotic frequencies
            freqs = [self.freqs[i], self.freqs[i]*1.5, self.freqs[i]*2.0]
            for f in freqs:
                chaotic_structure += np.sin(f * x_scaled[i]) * np.cos(f * x_scaled[i]**2)
        
        # Combine all components
        result = (gradient**2 + 
                 0.5 * radial_term + 
                 self.coupling_strength * coupling + 
                 0.3 * radial_decay + 
                 0.2 * chaotic_structure)
        
        # Add dimensionality-dependent noise
        noise_amp = 0.01 * (1.0 + 0.05 * np.sin(self.dim))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise