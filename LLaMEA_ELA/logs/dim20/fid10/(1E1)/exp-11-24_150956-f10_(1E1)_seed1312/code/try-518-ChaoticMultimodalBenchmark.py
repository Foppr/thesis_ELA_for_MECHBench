import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic logistic map component with delayed feedback
        chaotic = np.sum(4.0 * x_scaled * (1.0 - x_scaled) + 
                        0.3 * np.sin(2.0 * np.pi * x_scaled) * 
                        np.cos(1.5 * np.pi * x_scaled))
        
        # Hyperbolic tangent nonlinearities with varying parameters
        tanh_terms = np.sum(np.tanh(3.0 * x_scaled**2) + 
                           0.7 * np.tanh(2.5 * x_scaled**3) + 
                           0.4 * np.tanh(4.0 * x_scaled**4))
        
        # Fractal-like self-similarity with recursive scaling
        fractal = np.sum(np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled) + 
                        0.5 * np.sin(12.0 * x_scaled**2) * np.cos(10.0 * x_scaled**2) + 
                        0.3 * np.sin(16.0 * x_scaled**3) * np.cos(14.0 * x_scaled**3))
        
        # Time-delayed feedback with exponential decay
        delay_feedback = np.sum(np.exp(-2.0 * np.abs(x_scaled)) * 
                              np.sin(5.0 * x_scaled + 0.5 * np.sin(3.0 * x_scaled)))
        
        # Cross-dimensional coupling with polynomial interactions
        cross_coupling = np.sum((x_scaled[:-1]**2 + x_scaled[1:]**2) * 
                              np.exp(-0.5 * (x_scaled[:-1] - x_scaled[1:])**2) + 
                              (x_scaled[:-2]**3 + x_scaled[2:]**3) * 
                              np.sin(2.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Multi-scale harmonic interference with varying amplitudes
        harmonics = np.sum(np.sin(7.0 * x_scaled) * np.cos(9.0 * x_scaled) + 
                         0.6 * np.sin(11.0 * x_scaled**2) * np.cos(13.0 * x_scaled**2) + 
                         0.4 * np.sin(15.0 * x_scaled**3) * np.cos(17.0 * x_scaled**3))
        
        # Asymmetric weighting and normalization
        return (0.25 * chaotic + 0.2 * tanh_terms + 0.15 * fractal + 
                0.15 * delay_feedback + 0.1 * cross_coupling + 0.15 * harmonics + 1.8)