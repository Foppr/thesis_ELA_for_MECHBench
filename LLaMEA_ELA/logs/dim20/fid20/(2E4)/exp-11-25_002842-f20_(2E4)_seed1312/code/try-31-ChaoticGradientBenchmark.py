import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] for trigonometric components
        scaled_x = x * np.pi / 5.0
        
        # Exponentially decaying harmonic potentials with chaotic modulation
        harmonic_potential = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(5 * scaled_x) * np.cos(3 * scaled_x))
        
        # Multi-scale fractal-like ridge structure with varying curvature
        ridge_structure = 0.5 * np.sum((np.sin(2 * x) + 0.5 * np.sin(4 * x) + 0.25 * np.sin(8 * x)) ** 2)
        
        # Asymmetric basin components with different scaling in positive and negative directions
        asymmetric_basin = (0.3 * np.sum(np.where(x >= 0, x**2, 0.5 * x**2)) + 
                           0.2 * np.sum(np.where(x < 0, x**2, 0.5 * x**2)))
        
        # Chaotic gradient component with non-linear coupling between dimensions
        chaotic_gradient = 0.1 * np.sum(np.sin(np.exp(x[:-1]) + np.cos(x[1:])) * np.cos(np.exp(x[1:]) + np.sin(x[:-1])))
        
        # Multi-modal perturbation with varying amplitude and frequency based on dimension
        multimodal_perturbation = 0.05 * np.sum((np.sin(10 * x) + 0.3 * np.sin(25 * x)) * np.exp(-0.05 * np.abs(x)))
        
        # Cross-dimensional coupling with exponential decay and power-law scaling
        cross_coupling = 0.08 * np.sum(np.exp(-np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Fractal-like self-similarity component with recursive harmonic structure
        fractal_component = 0.03 * np.sum(np.sin(3 * np.sin(3 * scaled_x)) * np.cos(3 * np.cos(3 * scaled_x)))
        
        return harmonic_potential + ridge_structure + asymmetric_basin + chaotic_gradient + multimodal_perturbation + cross_coupling + fractal_component