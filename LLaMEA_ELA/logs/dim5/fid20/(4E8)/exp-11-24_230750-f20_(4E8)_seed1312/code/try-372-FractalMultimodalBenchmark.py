import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal hierarchical structure with self-similarity
        fractal = 0.0
        for i in range(self.dim):
            # Multi-scale periodic components with varying frequencies
            scale1 = np.sin(2.0 * x[i]) + 0.5 * np.sin(4.0 * x[i])
            scale2 = np.sin(0.5 * x[i]) + 0.3 * np.sin(2.5 * x[i])
            scale3 = np.sin(0.1 * x[i]) + 0.1 * np.sin(1.2 * x[i])
            
            # Self-similar pattern with diminishing amplitude
            fractal += (scale1**2 + scale2**2 + scale3**2) * np.exp(-0.1 * np.abs(x[i]))
        
        # Dynamic phase transition regions with varying thresholds
        phase_transition = 0.0
        for i in range(self.dim):
            # Piecewise linear transitions with smooth curvature
            if x[i] < -2.0:
                phase_transition += (x[i] + 2.0)**3
            elif x[i] > 2.0:
                phase_transition += (x[i] - 2.0)**3
            else:
                # Intermediate region with periodic modulation
                phase_transition += np.sin(3.0 * x[i]) * np.exp(-0.5 * x[i]**2)
        
        # Multi-scale harmonic potential with adaptive coupling
        harmonic = 0.0
        for i in range(self.dim):
            # Multiple frequency components with dynamic amplitudes
            freq1 = 1.0 + 0.5 * np.sin(0.3 * x[i])
            freq2 = 2.0 + 0.8 * np.cos(0.4 * x[i])
            freq3 = 3.0 + 1.2 * np.sin(0.6 * x[i])
            
            amplitude1 = 1.0 + 0.3 * np.cos(0.5 * x[i])
            amplitude2 = 1.5 + 0.4 * np.sin(0.7 * x[i])
            amplitude3 = 2.0 + 0.6 * np.cos(0.8 * x[i])
            
            harmonic += (amplitude1 * np.sin(freq1 * x[i])**2 + 
                        amplitude2 * np.sin(freq2 * x[i])**2 + 
                        amplitude3 * np.sin(freq3 * x[i])**2)
        
        # Cross-dimensional interaction with fractal coupling strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Fractal-like coupling strength that depends on both variables
                coupling_strength = 1.0 + 0.5 * np.sin(0.2 * (x[i] + x[j]))
                coupling += coupling_strength * (np.abs(x[i] - x[j])**1.5 + 
                                               np.abs(x[i] + x[j])**0.8)
        
        # Scale-invariant ruggedness with multiple resolution levels
        ruggedness = 0.0
        for i in range(self.dim):
            # Multiple resolution components
            res1 = np.sin(10.0 * x[i]) * np.exp(-0.05 * x[i]**2)
            res2 = np.sin(5.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            res3 = np.sin(2.0 * x[i]) * np.exp(-0.2 * x[i]**2)
            
            ruggedness += (res1**2 + res2**2 + res3**2) / 3.0
        
        # Dimensionally dependent normalization and scaling
        norm_factor = 1.0 + 0.1 * np.log(self.dim + 1) + 0.05 * np.sin(0.1 * self.dim)
        
        return (0.25 * fractal + 0.20 * phase_transition + 
                0.25 * harmonic + 0.20 * coupling + 0.10 * ruggedness) * norm_factor