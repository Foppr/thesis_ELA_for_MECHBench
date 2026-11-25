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
            
            # Asymmetric chaotic modulation
            term1 = np.sin(scale * x_norm[i] + phase) * np.cos(scale * x_norm[i]**2)
            term2 = np.sin(2.0 * scale * x_norm[i] + phase) * np.cos(3.0 * scale * x_norm[i]**2)
            
            # Add asymmetry through polynomial transformation
            asymmetry = 0.5 * (x_norm[i]**3 + 0.5 * x_norm[i]**5)
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
        
        # Cross-dimensional coupling with fractal-like interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Fractal-like coupling strength based on distance
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = np.exp(-dist * 2.0) * (1.0 + 0.3 * np.sin(7.0 * dist))
                coupling += coupling_strength * np.sin(4.0 * (x_norm[i] + x_norm[j]))
        
        # Scale-dependent ruggedness with self-similarity
        ruggedness = 0.0
        for i in range(self.dim):
            scale_factor = self.scales[min(i, len(self.scales)-1)]
            # Multi-scale sine waves creating rugged terrain
            for k in range(1, min(5, int(scale_factor * 5))):
                freq = k * scale_factor * 10.0
                ruggedness += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2) * (1.0 / (k + 1))
        
        # Combine all components with dynamic weighting
        position_dependent_weight = 1.0 + 0.5 * np.cos(np.sum(x_norm**2))
        result = (base * position_dependent_weight + 
                 1.2 * chaotic + 
                 0.8 * periodic + 
                 0.6 * direction_bias + 
                 0.9 * coupling + 
                 0.7 * ruggedness)
        
        # Add noise with chaotic characteristics
        noise_amp = 0.03 * (1.0 + 0.2 * np.sin(40.0 * np.sum(x_norm**2)))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise