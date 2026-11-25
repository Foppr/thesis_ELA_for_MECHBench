import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient component with logistic map modulation
        chaotic_grad = np.sum(np.sin(10 * x_norm) * np.cos(7 * x_norm) * 
                             (1 + 0.3 * np.sin(13 * x_norm)) * 
                             (1 + 0.2 * np.cos(9 * x_norm)))
        
        # Saddle point structure with hyperbolic tangent curvature
        saddle_points = np.sum(np.tanh(x_norm) * np.sinh(0.5 * x_norm) * 
                              (1 + 0.4 * np.cos(6 * x_norm)) * 
                              (1 + 0.3 * np.sin(8 * x_norm)))
        
        # Multi-scale harmonic interference with varying amplitudes
        harmonic_interference = np.sum(np.sin(5 * x_norm) * np.cos(4 * x_norm) * 
                                     (1 + 0.2 * np.sin(3 * x_norm)) * 
                                     (1 + 0.15 * np.cos(7 * x_norm)))
        
        # Non-uniform noise injection based on spatial position
        noise_injection = np.sum(0.1 * np.sin(20 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Varying curvature regions with piecewise power functions
        varying_curvature = np.sum(np.abs(x_norm)**(1.5 + 0.5 * np.sin(11 * x_norm)) * 
                                 (1 + 0.3 * np.cos(5 * x_norm)))
        
        # Cross-dimensional coupling with asymmetric interaction terms
        cross_coupling = np.sum((x_norm[:-1]**2 + x_norm[1:]**2) * 
                               np.exp(-0.1 * (x_norm[:-1] - x_norm[1:])**2) * 
                               (1 + 0.25 * np.sin(3 * x_norm[:-1])))
        
        # Combined landscape with diverse curvature and attraction regions
        return 2.0 * (chaotic_grad + saddle_points + harmonic_interference + 
                     noise_injection + varying_curvature + cross_coupling)