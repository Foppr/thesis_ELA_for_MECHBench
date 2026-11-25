import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic parameters with better distribution
        self.freqs = np.random.uniform(2.0, 15.0, dim)
        self.amps = np.random.uniform(0.3, 2.5, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.radial_freq = np.random.uniform(1.0, 4.0)
        self.coupling_strength = 0.4
        # Additional chaotic parameters for better structure
        self.multi_freqs = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Enhanced radial component with multiple chaotic oscillations
        r = np.sqrt(np.sum(x_scaled**2))
        radial_term = self.radial_freq * r * (np.sin(self.radial_freq * r) + 0.3 * np.cos(2 * self.radial_freq * r)) * np.exp(-0.1 * r**2)
        
        # Enhanced gradient component with modified sinusoidal modulation
        gradient = 0.0
        for i in range(self.dim):
            freq = self.freqs[i]
            amp = self.amps[i]
            phase = self.phase_shifts[i]
            
            # Modified modulation with higher harmonic components
            modulator = np.sin(freq * x_scaled[i] + phase) + 0.4 * np.cos(2 * freq * x_scaled[i] + phase) + 0.2 * np.sin(3 * freq * x_scaled[i] + phase)
            gradient += amp * x_scaled[i] * modulator
        
        # Improved cross-dimensional coupling with adaptive interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Adaptive chaotic coupling between dimensions
                coupling_term = np.sin(self.freqs[i] * x_scaled[i] + self.freqs[j] * x_scaled[j]) * np.cos(0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
                coupling += coupling_term * np.exp(-0.3 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Enhanced radial decay with oscillatory behavior
        radial_decay = np.exp(-r**2) * (np.sin(2 * r) + 0.5 * np.cos(4 * r))
        
        # Multi-scale chaotic structure with better frequency distribution
        chaotic_structure = 0.0
        for i in range(self.dim):
            # Multiple chaotic frequencies with varying weights
            freqs = [self.freqs[i], self.freqs[i]*1.3, self.freqs[i]*1.7, self.freqs[i]*2.3]
            weights = [1.0, 0.7, 0.5, 0.3]
            for f, w in zip(freqs, weights):
                chaotic_structure += w * np.sin(f * x_scaled[i]) * np.cos(f * x_scaled[i]**2)
        
        # Add multi-frequency radial component
        multi_radial = 0.0
        for i in range(self.dim):
            multi_radial += self.multi_freqs[i] * np.sin(self.multi_freqs[i] * r) * np.cos(self.multi_freqs[i] * r**2)
        
        # Combine all components with adjusted weights
        result = (gradient**2 + 
                 0.6 * radial_term + 
                 self.coupling_strength * coupling + 
                 0.4 * radial_decay + 
                 0.3 * chaotic_structure + 
                 0.1 * multi_radial)
        
        # Add dimensionality-dependent noise with better control
        noise_amp = 0.005 * (1.0 + 0.03 * np.sin(self.dim))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise