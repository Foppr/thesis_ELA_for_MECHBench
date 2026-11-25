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
            # Multi-frequency quantum-like oscillations with modified amplitudes
            quantum_chaos += (np.sin(xi * 35.0) * np.cos(xi * 28.0) * np.sin(xi * 22.0) + 
                             np.cos(xi * 40.0) * np.sin(xi * 18.0) * np.cos(xi * 12.0) +
                             np.sin(xi * 32.0) * np.cos(xi * 25.0) * np.sin(xi * 15.0)) / 3.0
        
        # Enhanced entanglement with quantum tunneling effects - modified interaction
        tunneling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quantum tunneling correlation with probabilistic scaling - altered probability function
                dist = np.abs(x_norm[i] - x_norm[j])
                tunnel_prob = 1.0 / (1.0 + np.exp(-dist * 10.0))  # Increased steepness
                corr_strength = np.exp(-dist**2 * 7.0) * np.sin(dist * np.pi * 4.0)  # Modified frequency
                tunneling += corr_strength * tunnel_prob * (x_norm[i]**3 + x_norm[j]**3)  # Changed power
        
        # Dynamic energy barriers with quantum-like potential wells - modified potential
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Quantum-like potential energy landscape - altered polynomial
            barriers += (xi**7 - 4.0 * xi**5 + 6.0 * xi**3 - 4.0 * xi) * np.exp(-0.3 * xi**2)
        
        # Probabilistic tunneling with fractal basin boundaries - modified function
        tunnel_basins = 0.0
        for i in range(self.dim):
            # Tunneling probability with discrete quantum states - altered frequency
            tunnel_prob = np.exp(-np.abs(x_norm[i]) * 7.0) * np.sin(x_norm[i] * 30.0)
            tunnel_basins += tunnel_prob
        
        # Quantum amplitude modulation with phase interference
        amp_modulation = 1.0 + 0.6 * np.sin(self.dim * 0.9) * np.cos(self.dim * 0.5) * np.exp(-self.dim * 0.04)
        
        # Dynamic quantum weights with superposition states - adjusted weights
        weight_quantum = 0.25 + 0.18 * np.sin(self.dim * 0.7)
        weight_tunneling = 0.35 + 0.15 * np.cos(self.dim * 0.6)
        weight_barriers = 0.25 + 0.12 * np.sin(self.dim * 0.5)
        weight_basins = 0.15 + 0.18 * np.cos(self.dim * 0.4)
        
        return amp_modulation * (weight_quantum * quantum_chaos + 
                                weight_tunneling * tunneling + 
                                weight_barriers * barriers + 
                                weight_basins * tunnel_basins)