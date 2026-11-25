import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-inspired entanglement with time-varying phase interference
        quantum_entanglement = 0
        for i in range(self.dim):
            phase_i = np.sin(0.5 * x[i] + self.dim * 0.1) * np.cos(0.3 * x[i] + self.dim * 0.2)
            entangle_factor = np.sin(0.4 * x[i] + phase_i) * np.cos(0.6 * x[i] + phase_i)
            quantum_entanglement += entangle_factor * np.exp(-0.1 * x[i]**2)
        
        # Dynamic chaotic coupling with adaptive weights and fractal scaling
        chaotic_coupling = 0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(0.7 * x[i] + self.dim * 0.3)
            scale_factor = 1.0 + 0.2 * np.cos(0.4 * x[i] + 0.5 * self.dim)
            for j in range(i+1, min(i+4, self.dim)):
                dist = (x[i] - x[j])**2
                coupling_term = weight * scale_factor * np.exp(-0.3 * dist) * np.sin(2.0 * dist)
                chaotic_coupling += coupling_term
        
        # Multi-scale oscillatory components with quantum tunneling behavior
        tunneling_oscillatory = 0
        for i in range(self.dim):
            freq1 = 1.5 + 1.0 * np.sin(0.3 * x[i] + 0.1 * self.dim)
            freq2 = 2.5 + 1.5 * np.cos(0.4 * x[i] + 0.2 * self.dim)
            freq3 = 3.5 + 2.0 * np.sin(0.5 * x[i] + 0.3 * self.dim)
            tunneling_oscillatory += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]**2) * np.exp(-0.2 * x[i]**2) * np.sin(freq3 * x[i]**3)
        
        # Adaptive ridge structures with dynamic conditioning
        adaptive_ridge = 0
        for i in range(self.dim):
            ridge_height = 1.0 + 0.8 * np.cos(0.6 * x[i] + 0.4 * self.dim)
            ridge_width = 0.5 + 0.3 * np.sin(0.5 * x[i])
            adaptive_ridge += ridge_height * np.exp(-0.5 * (x[i] / ridge_width)**2) * np.sin(4.0 * x[i])
        
        # Asymmetric multimodal structure with quantum-like tunneling
        asymmetric_tunnel = 0
        for i in range(self.dim):
            term1 = np.exp(-0.3 * (x[i] - 1.5)**2) * np.sin(2.5 * x[i]) * np.cos(0.5 * x[i])
            term2 = np.exp(-0.4 * (x[i] + 1.5)**2) * np.cos(3.0 * x[i]) * np.sin(0.7 * x[i])
            term3 = np.exp(-0.2 * x[i]**2) * np.sin(5.0 * x[i]**2) * np.cos(0.3 * x[i]**2)
            asymmetric_tunnel += term1 + term2 + term3
        
        # Combine all components with optimized weights and quantum scaling
        total = 0.2 * quantum_entanglement + 0.3 * chaotic_coupling + 0.25 * tunneling_oscillatory + 0.15 * adaptive_ridge + 0.1 * asymmetric_tunnel
        
        # Add time-varying chaotic modulation to global scaling
        time_factor = 1.0 + 0.3 * np.sin(0.2 * self.dim + 0.1 * np.sum(x))
        return total * time_factor