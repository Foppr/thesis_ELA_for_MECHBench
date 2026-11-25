import numpy as np

class QuantumSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Base quantum-like interference pattern with nested fractal components
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Nested fractal frequencies with quantum-like scaling
            freq1 = 3.0 + 2.0 * np.sin(0.4 * self.t + i * 0.25)
            freq2 = 1.5 + 1.0 * np.cos(0.6 * self.t + i * 0.3)
            amp1 = 1.2 + 0.6 * np.sin(0.3 * self.t + i * 0.4)
            amp2 = 0.8 + 0.4 * np.cos(0.5 * self.t + i * 0.35)
            
            # Quantum interference terms with nested scaling
            result += amp1 * np.sin(freq1 * xi) * np.cos(freq2 * xi**2) + \
                     amp2 * np.cos(freq1 * xi**3) * np.sin(freq2 * xi)
            
        # Quantum tunneling ridges with adaptive connectivity
        tunnel_strength = 2.0 + 1.0 * np.sin(0.8 * self.t)
        for i in range(self.dim):
            for j in range(max(0, i-2), min(i+2, self.dim)):  # Local coupling
                if i != j:
                    dist = (x[i] - x[j])**2 + 0.1
                    # Quantum tunneling interaction with complex phase
                    phase = np.sin(0.5 * self.t + (i+j) * 0.2)
                    tunnel = tunnel_strength * np.exp(-dist/2.0) * \
                            np.sin(2.0 * (x[i] + x[j]) + phase)
                    result += tunnel * (x[i]**2 + x[j]**2 + 1.0)
                    
        # Adaptive basin connectivity with time-varying potential wells
        basin_factor = 1.0 + 0.5 * np.cos(0.9 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Basin terms with variable depth and width
            result += basin_factor * (xi**4) * np.sin(0.6 * xi + 0.2 * self.t)**2 + \
                     0.5 * (xi**6) * np.cos(0.4 * xi**2 + 0.3 * self.t)
            
        # Multi-scale quantum modulation with chaotic phase shifts
        mod_freq = 5.0 + 3.0 * np.sin(1.0 * self.t)
        mod_amp = 1.0 + 0.5 * np.cos(0.7 * self.t)
        modulation = 0.0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(0.8 * self.t + i * 0.5) + \
                         0.2 * np.cos(1.2 * self.t + i * 0.4)
            modulation += mod_amp * np.sin(mod_freq * x[i] + phase_shift) * \
                         (x[i]**3 + 0.5 * x[i]**5)
            
        # Adaptive weighting with quantum-inspired coefficients
        w1 = 0.6 + 0.15 * np.sin(0.4 * self.t)
        w2 = 0.3 + 0.1 * np.cos(0.5 * self.t)
        w3 = 0.1 + 0.05 * np.sin(0.6 * self.t)
        
        # Added quantum entanglement interaction term for enhanced multimodality
        entangle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum entanglement with complex phase coupling
                phase_coupling = np.sin(3.0 * (x[i] + x[j]) + 0.5 * self.t)
                entangle_term += 0.4 * np.sin(2.0 * (x[i]**2 + x[j]**2) + 0.8 * self.t) * \
                               (x[i] * x[j]) * phase_coupling
        
        # Mutation: Slightly increased the influence of higher-order terms and added a new chaotic interaction component
        result = w1 * result + w2 * modulation + w3 * entangle_term
        
        # New chaotic interaction term with modified coupling strength
        chaos_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Modified phase coupling with increased nonlinearity
                phase_mod = np.sin(4.0 * (x[i] - x[j]) + 0.7 * self.t) + \
                           0.3 * np.cos(2.0 * (x[i] + x[j]) + 0.9 * self.t)
                chaos_interaction += 0.25 * (x[i]**3 + x[j]**3) * phase_mod
        
        result += chaos_interaction
        
        return result