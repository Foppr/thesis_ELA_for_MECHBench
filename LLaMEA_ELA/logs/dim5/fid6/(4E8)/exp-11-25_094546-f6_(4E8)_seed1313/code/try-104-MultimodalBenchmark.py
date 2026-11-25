import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-inspired chaotic component with entanglement
        quantum_chaos = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-frequency quantum-like oscillations
            quantum_chaos += (np.sin(xi * 30.0) * np.cos(xi * 25.0) * np.sin(xi * 20.0) + 
                             np.cos(xi * 35.0) * np.sin(xi * 15.0) * np.cos(xi * 10.0) +
                             np.sin(xi * 28.0) * np.cos(xi * 22.0) * np.sin(xi * 12.0)) / 3.0
        
        # Enhanced entanglement with quantum tunneling effects
        tunneling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum tunneling correlation with probabilistic scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                tunnel_prob = 1.0 / (1.0 + np.exp(-dist * 8.0))
                corr_strength = np.exp(-dist**2 * 5.0) * np.sin(dist * np.pi * 3.0)
                tunneling += corr_strength * tunnel_prob * (x_norm[i]**4 + x_norm[j]**4)
        
        # Dynamic energy barriers with quantum-like potential wells
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Quantum-like potential energy landscape
            barriers += (xi**6 - 3.0 * xi**4 + 3.0 * xi**2 - 1.0) * np.exp(-0.4 * xi**2)
        
        # Probabilistic tunneling with fractal basin boundaries
        tunnel_basins = 0.0
        for i in range(self.dim):
            # Tunneling probability with discrete quantum states
            tunnel_prob = np.exp(-np.abs(x_norm[i]) * 6.0) * np.sin(x_norm[i] * 25.0)
            tunnel_basins += tunnel_prob
        
        # Quantum amplitude modulation with phase interference
        amp_modulation = 1.0 + 0.7 * np.sin(self.dim * 0.8) * np.cos(self.dim * 0.4) * np.exp(-self.dim * 0.03)
        
        # Dynamic quantum weights with superposition states
        weight_quantum = 0.3 + 0.15 * np.sin(self.dim * 0.6)
        weight_tunneling = 0.3 + 0.2 * np.cos(self.dim * 0.5)
        weight_barriers = 0.2 + 0.1 * np.sin(self.dim * 0.4)
        weight_basins = 0.2 + 0.1 * np.cos(self.dim * 0.3)
        
        return amp_modulation * (weight_quantum * quantum_chaos + 
                                weight_tunneling * tunneling + 
                                weight_barriers * barriers + 
                                weight_basins * tunnel_basins)