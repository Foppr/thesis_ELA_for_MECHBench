import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced quantum chaotic component with adaptive scaling
        quantum_chaos = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-frequency quantum-like oscillations with amplitude modulation
            freqs = [32.0, 27.0, 22.0, 18.0]
            amplitudes = [1.0, 0.8, 0.6, 0.4]
            oscillation = sum(amplitudes[j] * np.sin(xi * freqs[j]) * np.cos(xi * (freqs[j] * 0.7)) 
                            for j in range(len(freqs)))
            quantum_chaos += oscillation / len(freqs)
        
        # Enhanced entanglement with dynamic correlation weights
        tunneling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x_norm[i] - x_norm[j])
                # Dynamic tunneling probability with adaptive scaling
                tunnel_prob = 1.0 / (1.0 + np.exp(-dist * 10.0))
                corr_strength = np.exp(-dist**2 * 7.0) * np.sin(dist * np.pi * 4.0)
                # Enhanced entanglement with dimension-dependent weights
                dim_weight = 1.0 + 0.3 * np.sin(self.dim * 0.5)
                tunneling += corr_strength * tunnel_prob * (x_norm[i]**3 + x_norm[j]**3) * dim_weight
        
        # Dynamic energy barriers with enhanced potential wells
        barriers = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Enhanced quantum-like potential with multiple minima
            barriers += (xi**8 - 4.0 * xi**6 + 6.0 * xi**4 - 4.0 * xi**2 + 1.0) * np.exp(-0.5 * xi**2)
        
        # Improved tunneling basins with fractal boundary detection
        tunnel_basins = 0.0
        for i in range(self.dim):
            # Enhanced tunneling probability with quantum state interference
            tunnel_prob = np.exp(-np.abs(x_norm[i]) * 8.0) * np.sin(x_norm[i] * 30.0)
            # Add dimension-dependent modulation
            mod_factor = 1.0 + 0.2 * np.cos(self.dim * 0.3)
            tunnel_basins += tunnel_prob * mod_factor
        
        # Enhanced amplitude modulation with quantum phase interference
        amp_modulation = 1.0 + 0.8 * np.sin(self.dim * 0.9) * np.cos(self.dim * 0.5) * np.exp(-self.dim * 0.04)
        
        # Dynamic quantum weights with superposition state adaptation
        weight_quantum = 0.35 + 0.2 * np.sin(self.dim * 0.7)
        weight_tunneling = 0.35 + 0.18 * np.cos(self.dim * 0.6)
        weight_barriers = 0.25 + 0.12 * np.sin(self.dim * 0.5)
        weight_basins = 0.25 + 0.15 * np.cos(self.dim * 0.4)
        
        return amp_modulation * (weight_quantum * quantum_chaos + 
                                weight_tunneling * tunneling + 
                                weight_barriers * barriers + 
                                weight_basins * tunnel_basins)