import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator-inspired interactions
        quantum_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum coupling with phase modulation
                phase = np.sin(0.3 * x[i]) * np.cos(0.4 * x[j])
                amp = 1.0 + 0.2 * np.sin(0.5 * (x[i] + x[j]))
                freq = 2.0 + 0.3 * np.cos(0.6 * x[i])
                quantum_interaction += amp * np.sin(freq * (x[i] - x[j]) + phase) / (1.0 + (x[i] - x[j])**2)
        
        # Adaptive fractal gradient components with dynamic scaling
        fractal_grad = 0
        for i in range(self.dim):
            # Fractal-like behavior with dimension-dependent scaling
            scale = 1.0 + 0.5 * np.sin(0.4 * i)
            freq = 3.0 + 0.2 * np.cos(0.3 * x[i])
            fractal_grad += scale * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2) * np.cos(0.5 * x[i]**2)
        
        # Dynamic coupling terms with time-varying coefficients
        dynamic_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Time-varying coupling with exponential decay
                t = 0.5 * (i + j)
                coeff = np.exp(-0.2 * t) * (1.0 + 0.3 * np.sin(0.4 * t))
                dynamic_coupling += coeff * np.cos(x[i] * x[j]) * np.sin(0.3 * (x[i]**2 + x[j]**2))
        
        # Saddle-point valleys with complex curvature
        saddle_valleys = 0
        for i in range(self.dim):
            # Multi-saddle structure with varying coefficients
            a = 1.5 + 0.3 * np.sin(0.5 * x[i])
            b = 1.0 + 0.2 * np.cos(0.4 * x[i])
            c = 0.8 + 0.1 * np.sin(0.6 * x[i])
            saddle_valleys += (x[i]**2 - a) * (x[i]**2 - b) * (x[i]**2 - c)
        
        # Spectral Gaussian kernel with quantum-inspired modulation
        spectral_gauss = 0
        for i in range(self.dim):
            # Quantum-modulated Gaussian with complex frequency
            freq = 1.5 + 0.4 * np.sin(0.7 * x[i])
            width = 0.2 + 0.1 * np.cos(0.3 * x[i])
            center = 0.5 * np.sin(0.6 * x[i]) + 0.3 * np.cos(0.8 * x[i])
            spectral_gauss += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.sin(freq * x[i]) * np.cos(0.4 * x[i])
        
        # Cross-dimensional chaotic interactions with quaternion-inspired terms
        cross_chaos = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quaternion-like coupling with chaotic modulation
                mod = np.sin(x[i]) * np.cos(x[j]) + np.cos(x[i]) * np.sin(x[j])
                chaos = np.tan(0.5 * (x[i] + x[j])) / (1.0 + 0.2 * (x[i] - x[j])**2)
                cross_chaos += mod * chaos
        
        # Global conditioning with quantum-inspired scaling
        cond_factor = 1.0 + 0.4 * np.sin(0.5 * self.dim) + 0.2 * np.cos(0.7 * self.dim) + 0.1 * np.sin(0.3 * self.dim)
        
        # Combine all components with optimized weights
        return cond_factor * (0.2 * quantum_interaction + 0.2 * fractal_grad + 
                             0.15 * dynamic_coupling + 0.15 * saddle_valleys + 
                             0.15 * spectral_gauss + 0.15 * cross_chaos)