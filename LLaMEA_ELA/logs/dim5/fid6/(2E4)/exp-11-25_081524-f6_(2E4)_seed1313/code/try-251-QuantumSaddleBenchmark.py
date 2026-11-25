import numpy as np

class QuantumSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base quantum-like interference pattern
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Quantum frequency modulation with phase coherence
            freq = 3.0 + 2.0 * np.sin(0.6 * self.t + i * 0.4)
            amp = 1.5 + 0.7 * np.cos(0.5 * self.t + i * 0.3)
            # Interference pattern with complex exponential components
            result += amp * (xi**2) * np.sin(freq * xi + 0.3 * self.t) * np.cos(0.4 * xi**3 + 0.2 * self.t)
            
        # Chaotic saddle point structures with adaptive basin connectivity
        saddle_strength = 2.0 + 0.8 * np.sin(0.7 * self.t)
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Extended coupling range
                # Saddle-like interaction with quantum tunneling effects
                dist = (x[i] - x[j])**2 + 0.1 * np.sin(0.5 * self.t + i + j)
                saddle = saddle_strength * np.exp(-dist/2.0) * np.cos(2.0 * (x[i] - x[j]) + 0.6 * self.t)
                result += saddle * (x[i]**2 + x[j]**2 + 0.5 * np.sin(0.8 * self.t + i * j))
                
        # Time-varying quantum-like elliptic shaping with dynamic eccentricity
        ellipse_factor = 0.8 + 0.6 * np.cos(0.9 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Quantum elliptic terms with phase-modulated eccentricity
            result += ellipse_factor * (xi**3) * np.sin(0.7 * xi + 0.4 * self.t) * np.cos(0.5 * xi**2 + 0.3 * self.t)
            
        # Multi-scale quantum interference modulation with tunable coupling strength
        coupling_strength = 1.2 + 0.6 * np.sin(0.8 * self.t)
        mod_freq = 5.0 + 3.0 * np.cos(0.7 * self.t)
        mod_amp = 1.0 + 0.5 * np.sin(0.9 * self.t)
        modulation = 0.0
        for i in range(self.dim):
            phase_shift = 0.6 * np.cos(0.7 * self.t + i * 0.5)
            modulation += mod_amp * np.cos(mod_freq * x[i] + phase_shift) * (x[i]**2 + 0.3 * np.sin(0.6 * self.t + i))
            
        # Adaptive quantum weighting
        w1 = 0.8 + 0.1 * np.cos(0.6 * self.t)
        w2 = 0.15 + 0.08 * np.sin(0.7 * self.t)
        w3 = 0.05 + 0.03 * np.cos(0.8 * self.t)
        
        # Added quantum entanglement term for enhanced multimodality
        entangle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum correlation with tunable strength
                correlation = np.sin(3.0 * (x[i] + x[j]) + 0.4 * self.t) * np.cos(1.5 * (x[i] - x[j]) + 0.3 * self.t)
                entangle_term += coupling_strength * correlation * (x[i]**2 * x[j]**2)
        
        result = w1 * result + w2 * modulation + w3 * entangle_term
        return result