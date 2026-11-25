import numpy as np

class WaveRBFNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Wave components with varying frequencies and amplitudes
        self.wave_freq = np.random.uniform(1.0, 8.0, size=dim)
        self.wave_amp = np.random.uniform(0.5, 3.0, size=dim)
        self.wave_phase = np.random.uniform(0, 2*np.pi, size=dim)
        
        # Radial basis functions with random centers and widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, size=(15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, size=15)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, size=15)
        
        # Adaptive noise parameters
        self.noise_amplitude = np.random.uniform(0.1, 1.5, size=dim)
        self.noise_frequency = np.random.uniform(0.5, 5.0, size=dim)
        self.noise_decay = np.random.uniform(0.1, 0.8, size=dim)
        
        # Interaction weights between dimensions
        self.interaction_strength = np.random.uniform(0.1, 2.0, size=(dim, dim))
        
        # Periodic modulation parameters
        self.mod_freq = np.random.uniform(0.1, 3.0, size=dim)
        self.mod_amp = np.random.uniform(0.1, 1.0, size=dim)
        
        # Multi-scale harmonic components
        self.harmonic_freqs = np.random.uniform(2.0, 12.0, size=dim)
        self.harmonic_amps = np.random.uniform(0.2, 1.5, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Wave interference component
        wave_component = 0.0
        for i in range(self.dim):
            wave_val = self.wave_amp[i] * np.sin(self.wave_freq[i] * x[i] + self.wave_phase[i])
            wave_component += wave_val
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(15):
            dist_sq = np.sum((x - self.rbf_centers[i]) ** 2)
            rbf_val = self.rbf_weights[i] * np.exp(-dist_sq / (2 * self.rbf_widths[i] ** 2))
            rbf_component += rbf_val
            
        # Adaptive noise component
        noise_component = 0.0
        for i in range(self.dim):
            # Noise with decay based on distance from center
            decay_factor = np.exp(-self.noise_decay[i] * np.abs(x[i]))
            noise_val = self.noise_amplitude[i] * np.sin(self.noise_frequency[i] * x[i]) * decay_factor
            noise_component += noise_val
            
        # Dimensional interaction component
        interaction_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    interaction_val = self.interaction_strength[i, j] * np.sin(x[i]) * np.cos(x[j])
                    interaction_component += interaction_val
                    
        # Periodic modulation component
        mod_component = 0.0
        for i in range(self.dim):
            mod_val = self.mod_amp[i] * np.cos(self.mod_freq[i] * x[i])
            mod_component += mod_val
            
        # Multi-scale harmonic component
        harmonic_component = 0.0
        for i in range(self.dim):
            harm_val = self.harmonic_amps[i] * np.sin(self.harmonic_freqs[i] * x[i])
            harmonic_component += harm_val
            
        # Combine all components with appropriate weights
        return (1.5 * wave_component + 
                1.2 * rbf_component + 
                0.8 * noise_component + 
                0.6 * interaction_component + 
                0.4 * mod_component + 
                0.3 * harmonic_component)