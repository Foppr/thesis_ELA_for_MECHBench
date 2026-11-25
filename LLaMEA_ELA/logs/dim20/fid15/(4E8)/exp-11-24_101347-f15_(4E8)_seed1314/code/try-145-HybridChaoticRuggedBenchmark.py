import numpy as np

class HybridChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scale factors and phase shifts for chaotic modulation
        self.scales = np.logspace(-1, 1, min(6, dim), base=10)
        self.phases = np.linspace(0, 2*np.pi, min(6, dim))
        self.amplitudes = np.logspace(0, -1, min(6, dim), base=10)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with directional bias
        base = np.sum(x_norm**2) * (1.0 + 0.3 * np.sin(np.sum(x_norm)))
        
        # Chaotic multi-modal component with asymmetric valleys
        chaotic = 0.0
        for i in range(self.dim):
            scale = self.scales[min(i, len(self.scales)-1)]
            phase = self.phases[min(i, len(self.phases)-1)]
            
            # Asymmetric chaotic modulation with modified parameters
            term1 = np.sin(scale * x_norm[i] + phase) * np.cos(scale * x_norm[i]**2)
            term2 = np.sin(2.0 * scale * x_norm[i] + phase) * np.cos(3.0 * scale * x_norm[i]**2)
            
            # Add asymmetry through polynomial transformation with different exponents
            asymmetry = 0.5 * (x_norm[i]**3 + 0.3 * x_norm[i]**7)
            chaotic += (term1 + term2) * (1.0 + 0.4 * asymmetry)
        
        # Periodic ridge structure with scale-dependent frequency
        periodic = 0.0
        for i in range(self.dim):
            scale = self.scales[min(i, len(self.scales)-1)]
            freq = 8.0 * scale
            
            # Create ridges using sine waves with varying amplitudes
            ridge = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2)
            periodic += ridge * self.amplitudes[min(i, len(self.amplitudes)-1)]
        
        # Directional bias component - encourages movement in specific directions
        direction_bias = 0.0
        for i in range(min(3, self.dim)):
            if i < self.dim - 1:
                direction_bias += (x_norm[i] * x_norm[i+1]) * np.sin(5.0 * (x_norm[i] + x_norm[i+1]))
        
        # Enhanced cross-dimensional coupling with stronger fractal-like interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Fractal-like coupling strength based on distance with modified parameters
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = np.exp(-dist * 3.0) * (1.0 + 0.4 * np.sin(9.0 * dist))
                coupling += coupling_strength * np.sin(5.0 * (x_norm[i] + x_norm[j]))
        
        # Scale-dependent ruggedness with self-similarity and modified frequencies
        ruggedness = 0.0
        for i in range(self.dim):
            scale_factor = self.scales[min(i, len(self.scales)-1)]
            # Multi-scale sine waves creating rugged terrain with different frequency multipliers
            for k in range(1, min(5, int(scale_factor * 7))):
                freq = k * scale_factor * 12.0
                ruggedness += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2) * (1.0 / (k + 2))
        
        # Combine all components with dynamic weighting
        position_dependent_weight = 1.0 + 0.5 * np.cos(np.sum(x_norm**2))
        result = (base * position_dependent_weight + 
                 1.3 * chaotic + 
                 0.9 * periodic + 
                 0.7 * direction_bias + 
                 1.0 * coupling + 
                 0.8 * ruggedness)
        
        # Add noise with chaotic characteristics
        noise_amp = 0.03 * (1.0 + 0.2 * np.sin(40.0 * np.sum(x_norm**2)))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise