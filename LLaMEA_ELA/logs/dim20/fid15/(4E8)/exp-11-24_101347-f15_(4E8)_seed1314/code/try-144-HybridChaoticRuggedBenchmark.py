import numpy as np

class HybridChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute enhanced chaotic parameters with fractal scaling
        self.scales = np.logspace(-1.5, 1.5, min(8, dim), base=10)
        self.phases = np.linspace(0, 4*np.pi, min(8, dim))
        self.amplitudes = np.logspace(-0.5, -2, min(8, dim), base=10)
        # Add fractal dimension scaling
        self.fractal_dims = np.linspace(0.3, 1.7, min(8, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1] range with adaptive scaling
        x_norm = x / 5.0
        
        # Enhanced base quadratic term with fractal modulation
        base = np.sum(x_norm**2) * (1.0 + 0.5 * np.sin(np.sum(x_norm)) * np.cos(3.0 * np.sum(x_norm**2)))
        
        # Enhanced chaotic multi-modal component with fractal asymmetry
        chaotic = 0.0
        for i in range(self.dim):
            scale = self.scales[min(i, len(self.scales)-1)]
            phase = self.phases[min(i, len(self.phases)-1)]
            fractal_dim = self.fractal_dims[min(i, len(self.fractal_dims)-1)]
            
            # Fractal chaotic modulation with multi-frequency components
            term1 = np.sin(scale * x_norm[i] + phase) * np.cos(scale * x_norm[i]**2)
            term2 = np.sin(2.0 * scale * x_norm[i] + phase) * np.cos(3.0 * scale * x_norm[i]**2)
            term3 = np.sin(5.0 * scale * x_norm[i] + phase) * np.cos(7.0 * scale * x_norm[i]**3)
            
            # Fractal asymmetry through power law transformation
            asymmetry = 0.3 * (x_norm[i]**(2.0 + fractal_dim) + 0.2 * x_norm[i]**(4.0 + fractal_dim))
            chaotic += (term1 + term2 + term3) * (1.0 + 0.6 * asymmetry)
        
        # Enhanced periodic ridge structure with fractal frequency
        periodic = 0.0
        for i in range(self.dim):
            scale = self.scales[min(i, len(self.scales)-1)]
            freq = 12.0 * scale
            
            # Create complex ridges using multi-frequency sine waves
            ridge = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2) + \
                   0.5 * np.sin(2*freq * x_norm[i]) * np.cos(3*freq * x_norm[i]**2)
            periodic += ridge * self.amplitudes[min(i, len(self.amplitudes)-1)]
        
        # Enhanced directional bias component with fractal coupling
        direction_bias = 0.0
        for i in range(min(4, self.dim)):
            if i < self.dim - 1:
                # Fractal directional coupling strength
                coupling_strength = (1.0 + 0.4 * np.sin(5.0 * (x_norm[i] + x_norm[i+1]))) * \
                                  np.exp(-np.abs(x_norm[i] - x_norm[i+1]) * 3.0)
                direction_bias += coupling_strength * (x_norm[i] * x_norm[i+1]) * \
                                np.sin(7.0 * (x_norm[i] + x_norm[i+1]))
        
        # Enhanced cross-dimensional coupling with multi-scale fractal interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                # Multi-scale fractal coupling strength based on distance and dimension
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling_strength = np.exp(-dist * 3.0) * (1.0 + 0.5 * np.sin(9.0 * dist)) * \
                                  (1.0 + 0.3 * np.cos(4.0 * dist**2))
                coupling += coupling_strength * np.sin(6.0 * (x_norm[i] + x_norm[j]))
        
        # Enhanced scale-dependent ruggedness with multi-fractal self-similarity
        ruggedness = 0.0
        for i in range(self.dim):
            scale_factor = self.scales[min(i, len(self.scales)-1)]
            # Multi-scale fractal sine waves creating complex terrain
            for k in range(1, min(7, int(scale_factor * 8))):
                freq = k * scale_factor * 15.0
                ruggedness += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]**2) * \
                            (1.0 / (k + 2)) * (1.0 + 0.4 * np.sin(3.0 * k * x_norm[i]))
        
        # Enhanced dynamic weighting with fractal modulation
        position_dependent_weight = 1.0 + 0.7 * np.cos(np.sum(x_norm**2)) * \
                                 np.sin(5.0 * np.sum(x_norm**2))
        result = (base * position_dependent_weight + 
                 1.5 * chaotic + 
                 1.0 * periodic + 
                 0.8 * direction_bias + 
                 1.2 * coupling + 
                 1.1 * ruggedness)
        
        # Enhanced noise with fractal characteristics
        noise_amp = 0.05 * (1.0 + 0.3 * np.sin(50.0 * np.sum(x_norm**2)))
        noise = noise_amp * np.random.normal(0.0, 1.0)
        
        return result + noise