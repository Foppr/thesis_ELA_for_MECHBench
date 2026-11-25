import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quantum-like interference component with dynamic phase
        quantum = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create quantum interference patterns with multiple frequencies
            phase = np.pi * xi * (1.0 + 0.3 * np.sin(2.0 * xi))
            quantum += np.sin(15.0 * xi + phase) * np.cos(10.0 * xi - phase) * np.exp(-0.3 * xi**2)
        
        # Dynamic phase shift component with adaptive frequency
        phaseshift = 0.0
        for i in range(self.dim):
            # Add dynamic phase that depends on position and dimension
            base_freq = 8.0 + 3.0 * np.sin(0.5 * x_norm[i])
            shift = np.cos(4.0 * x_norm[i]) * np.sin(5.0 * x_norm[i])
            phaseshift += np.sin(base_freq * x_norm[i] + shift) * np.exp(-0.2 * x_norm[i]**2)
        
        # Adaptive dimension coupling with fractal-like scaling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use fractal-like distance metric with adaptive scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                scale = 1.0 + 0.6 * np.sin(12.0 * dist)
                coupling += scale * np.sin(18.0 * dist) * np.exp(-dist**3)
        
        # Sharp transition component with adaptive threshold
        sharp = 0.0
        for i in range(self.dim):
            # Add sharp transitions near critical points
            critical_points = [0.25, -0.35, 0.75, -0.85, 0.1]
            min_dist = min([np.abs(x_norm[i] - cp) for cp in critical_points])
            sharp += np.exp(-15.0 * min_dist**2) * np.cos(25.0 * x_norm[i])
        
        # Multi-scale harmonic component with self-similar patterns
        multiscale = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Create multi-frequency harmonics with varying amplitudes
            freqs = [1.5, 3.5, 7.5, 11.5]
            amps = [1.2, 0.8, 0.5, 0.3]
            for f, a in zip(freqs, amps):
                multiscale += a * np.sin(f * xi) * np.exp(-0.1 * xi**2)
        
        # Combine all components with dynamic weights
        weight_quantum = 0.3 + 0.08 * np.sin(self.dim * 0.15)
        weight_phaseshift = 0.25 + 0.1 * np.cos(self.dim * 0.1)
        weight_coupling = 0.25 + 0.05 * np.tanh(self.dim * 0.03)
        weight_sharp = 0.18 + 0.07 * np.sin(self.dim * 0.08)
        weight_multiscale = 0.15 + 0.05 * np.cos(self.dim * 0.06)
        
        return (weight_quantum * quantum + 
                weight_phaseshift * phaseshift + 
                weight_coupling * coupling + 
                weight_sharp * sharp + 
                weight_multiscale * multiscale)