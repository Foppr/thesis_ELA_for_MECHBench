import numpy as np

class FractalResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal harmonic interference with self-similar patterns
        fractal_harmonic = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-fractal frequency components with varying amplitudes
            freqs = [1.0, 2.5, 4.0, 7.5, 12.0]
            amps = [1.0, 0.6, 0.3, 0.2, 0.1]
            
            for freq, amp in zip(freqs, amps):
                # Fractal-like modulation using sine and cosine with scaling
                fractal_harmonic += amp * np.sin(freq * xi) * np.cos(freq * xi * 0.5) * np.exp(-0.5 * xi**2)
        
        # Adaptive gradient modulation based on dimensionality
        adaptive_grad = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Dimensionally dependent gradient strength with fractal scaling
            grad_strength = 1.0 + 0.5 * np.sin(0.2 * i * np.pi) + 0.3 * np.cos(0.1 * i * np.pi)
            adaptive_grad += grad_strength * (xi**6 - 3.0 * xi**4 + 2.0 * xi**2)
            
        # Resonance wells with dimensionally coupled coupling
        resonance_wells = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multiple resonance peaks with varying heights and widths
            peak1 = 2.0 * np.exp(-5.0 * (xi - 0.3)**2) * np.sin(10.0 * xi)
            peak2 = 1.5 * np.exp(-3.0 * (xi + 0.4)**2) * np.cos(15.0 * xi)
            peak3 = 1.0 * np.exp(-7.0 * (xi - 0.8)**2) * np.sin(20.0 * xi)
            
            # Coupling between dimensions using fractal-like interaction
            coupling_term = 0.0
            for j in range(self.dim):
                if i != j:
                    dist = np.abs(xi - x_norm[j])
                    coupling_strength = 0.1 + 0.2 * np.sin(0.3 * (i + j))
                    coupling_term += coupling_strength * np.exp(-dist**2 * 3.0) * np.sin(5.0 * dist)
            
            resonance_wells += (peak1 + peak2 + peak3 + coupling_term)
        
        # Multi-scale fractal dimension modulation
        fractal_dim = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Fractal-like scaling with multiple scales
            scale1 = 0.5 * np.exp(-0.5 * xi**2) * np.sin(3.0 * xi)
            scale2 = 0.3 * np.exp(-0.3 * xi**2) * np.cos(7.0 * xi)
            scale3 = 0.2 * np.exp(-0.7 * xi**2) * np.sin(11.0 * xi)
            fractal_dim += scale1 + scale2 + scale3
            
        # Dimensionally adaptive scaling factor
        scale_factor = 1.0 + 0.4 * np.sin(self.dim * 0.3) + 0.2 * np.cos(self.dim * 0.1)
        
        # Combine all components with optimized weights
        total = (0.35 * fractal_harmonic + 
                0.30 * adaptive_grad + 
                0.25 * resonance_wells + 
                0.10 * fractal_dim) * scale_factor
        
        return total