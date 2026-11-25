import numpy as np

class FractalQuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component with Hurst parameter modulation
        f1 = 0.0
        hurst = 0.3 + 0.4 * np.sin(0.25 * np.sum(x**2))
        for i in range(self.dim):
            # Simple fractal-like scaling
            scale = 1.0 / (1.0 + 0.1 * i)
            f1 += scale * np.sin(scale * x[i]) * np.cos(scale * x[i])
            
        # Adaptive elliptic conditioning with dynamic eccentricity
        f2 = 0.0
        for i in range(self.dim):
            eccentricity = 0.5 + 0.5 * np.sin(0.35 * i + 0.25 * np.sum(x**2))
            f2 += (x[i]**2) / (1.0 + eccentricity * np.cos(0.45 * x[i])**2)
            
        # Quantum-inspired harmonic interactions with phase modulation
        f3 = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            freq = 1.0 + 0.7 * np.cos(0.3 * i)
            f3 += np.sin(freq * x[i] + phase)**2 * np.exp(-0.15 * x[i]**2)
            
        # Multi-scale radial interactions with power-law decay
        f4 = 0.0
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            for i in range(self.dim):
                power = 1.5 + 0.5 * np.sin(0.2 * i)
                f4 += (x[i]**2) / (r**(power)) * np.exp(-0.1 * x[i]**2)
                
        # Cross-dimensional coupling with quantum entanglement-like terms
        f5 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = 0.5 + 0.3 * np.sin(0.4 * (i + j))
                    coupling = x[i] * x[j] * coupling_strength
                    coupling_sum += coupling
            f5 += coupling_sum * np.exp(-0.1 * x[i]**2)
            
        # Boundary-sensitive quantum tunneling effects
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                tunnel_prob = 0.3 + 0.2 * np.cos(0.5 * i)
                f6 += tunnel_prob * np.exp(-2.0 * (5.0 - np.abs(x[i]))**2)
                
        # Fractal harmonic resonance with self-similarity
        f7 = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.8 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            f7 += np.sin(freq * x[i])**2 * np.cos(freq * x[i])**2
            
        # Adaptive penalty with fractal dimension modulation
        f8 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 3.0:
                fractal_dim = 1.2 + 0.3 * np.cos(0.4 * i)
                f8 += (np.abs(x[i]) - 3.0)**fractal_dim
                
        # Multi-modal quantum-like interference patterns
        f9 = 0.0
        for i in range(self.dim):
            interference = 0.0
            for k in range(1, 4):
                phase_shift = k * np.pi / 4.0 + 0.2 * i
                interference += np.sin(k * x[i] + phase_shift) * np.cos(k * x[i] + phase_shift)
            f9 += interference**2
            
        # Scale-adaptive exponential conditioning with chaotic modulation
        f10 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * np.sum(x**2))
            f10 += np.exp(-scale_factor * x[i]**2) * np.sin(2.0 * x[i])**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10