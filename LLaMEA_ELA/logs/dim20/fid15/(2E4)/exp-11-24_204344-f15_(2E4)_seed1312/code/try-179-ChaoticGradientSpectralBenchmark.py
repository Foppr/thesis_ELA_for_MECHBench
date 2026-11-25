import numpy as np

class ChaoticGradientSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Chaotic gradient flow component with spectral band modulation
        gradient_flow = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.7) + 0.8 * np.cos(i * 0.9)
            phase = 0.5 + 0.3 * np.sin(i * 1.2)
            gradient_flow += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase * 1.3) * np.exp(-0.1 * x[i]**2)
        
        # Spectral band interactions with dynamic frequency coupling
        spectral_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_coupling = 1.0 + 0.5 * np.sin(x[i] * x[j] * 0.8)
                spectral_interaction += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(freq_coupling * (x[i] + x[j])) * np.cos(freq_coupling * (x[i] - x[j]))
        
        # Dynamic dimensionality reduction with adaptive scaling
        dim_reduction = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(i * 0.6) + 0.3 * np.cos(i * 0.8)
            dim_reduction += scale_factor * (x[i]**2 - 2.0 * x[i] + 1.0) * np.exp(-0.3 * x[i]**2)
        
        # Multi-scale chaotic oscillations with frequency modulation
        chaotic_oscillation = 0.0
        for i in range(self.dim):
            mod_freq = 5.0 + 3.0 * np.sin(i * 0.4) + 2.0 * np.cos(i * 0.6)
            chaotic_oscillation += np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i]) * np.exp(-0.2 * np.abs(x[i]))
        
        # Band-limited noise with chaotic amplitude modulation
        noise_component = 0.0
        for i in range(self.dim):
            amp_mod = 1.0 + 0.5 * np.sin(i * 0.3) * np.cos(i * 0.5)
            noise_component += amp_mod * np.sin(x[i] * np.pi * (1.0 + 0.2 * np.sin(i))) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional coupling with spectral filtering
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.3 * np.sin(i * j * 0.4)
                filter_freq = 2.0 + 1.0 * np.cos(i + j)
                cross_coupling += coupling_strength * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(filter_freq * (x[i] + x[j]))
        
        # Adaptive resonance with chaotic feedback
        resonance = 0.0
        for i in range(self.dim):
            feedback = 1.0 + 0.3 * np.sin(x[i] * 2.0)
            resonance += feedback * np.sin(x[i] * 3.0) * np.cos(x[i] * 1.5) * np.exp(-0.2 * x[i]**2)
        
        # Fractional dimensionality with dynamic scaling
        fractional_dim = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 1.2)
            fractional_dim += scale * (x[i]**3 - 3.0 * x[i]) * np.exp(-0.15 * x[i]**2)
        
        # Final chaotic combination with dynamic weights
        return 0.8 * gradient_flow + 0.9 * spectral_interaction + 0.7 * dim_reduction + \
               1.1 * chaotic_oscillation + 1.0 * noise_component + 0.6 * cross_coupling + \
               0.5 * resonance + 0.4 * fractional_dim